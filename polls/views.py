from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {
		'latest_question_list': latest_question_list
	}
	return render(request,'index.html', context)

def details(request, question_id):
	q = get_object_or_404(Question, pk=question_id)
	return render(request, 'details.html', {'q': q})

def results(request, question_id):
	q = get_object_or_404(Question, pk=question_id)
	return render(request, 'results.html', {'q':q})


def vote(request, question_id):
	q = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = q.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'details.html', {
			'q':q,
			'error_message': "You didn't select a chooice."
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))