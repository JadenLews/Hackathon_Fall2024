from django.db import models
from django.contrib.auth.models import User

class ProjectPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)  # Initialize likes to 0
    workers = models.IntegerField(default=1)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skills = models.JSONField()  # Store skills as a list of strings in JSON format

    def __str__(self):
        return self.title