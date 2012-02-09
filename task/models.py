from django.db import models
from django.forms import ModelForm

class Task(models.Model):
  title = models.CharField(max_length=200)
  done = models.BooleanField()

  def __unicode__(self):
  	return self.title

class TaskForm(ModelForm):
	class Meta:
		model = Task