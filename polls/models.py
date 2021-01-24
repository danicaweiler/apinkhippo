import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
	# Ensure each question is unique - case sensitive
    question_text = models.CharField(max_length=200, unique = True)
    pub_date = models.DateTimeField('date published')
	
    def __str__(self):
        return self.question_text
	
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

	# constrains choice to text to me unique per question - case sensitive
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['question', 'choice_text'], 
                name='unique choice'
            )
        ]
		
    def __str__(self):
        return self.choice_text