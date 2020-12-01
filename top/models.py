from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

