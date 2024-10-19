from django.db import models
from django.contrib.auth.models import User

class ProjectPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    workers = models.IntegerField(default=1)
    workersneeded = models.IntegerField(default=0)  # This is the new field
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skills = models.JSONField()

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django User
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
