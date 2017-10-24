import daytime
from django.test import TestCase
from django.utils import timezone
from .models import Question
# Create your tests here.


class QuestionModelTests(TestCase):
	def test_was_published_with_future_question(self):
		time = timezone.now()+ daytime.timedate(days=30)
		future_q = Question(pub_date=time)
		self.assertIs(future_q.was_published_recently(), False)