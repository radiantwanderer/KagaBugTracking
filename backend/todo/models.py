from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	resolved = models.BooleanField(default=False)
	#found_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

	def __str__(self):
		return self.title
