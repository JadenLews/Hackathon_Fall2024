from django.db import models
from django.contrib.auth.models import User

class ProjectPost(models.Model):
    title = models.CharField(max_length=100)
    description_long = models.TextField(null=True, blank=True)
    description = models.JSONField(default=list, blank=True) 
    skills = models.JSONField(default=list, blank=True) 
    likes = models.IntegerField(default=0)
    workers = models.IntegerField(default=1)
    workersneeded = models.IntegerField(default=2)  # This is the new field
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skills = models.JSONField(default=list, blank=True)
    categories = models.JSONField(default=list, blank=True)  

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    skills = models.JSONField(default=list, blank=True)  # Initialize to an empty list
    linkedin = models.URLField(max_length=200, blank=True)  
    git = models.URLField(max_length=200, blank=True)
    choice_site = models.URLField(max_length=200, blank=True)
    def __str__(self):
        return f'{self.user.username} Profile'
    
class Notifications(models.Model):
    requestor = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='requestor')
    post_owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    post = models.ForeignKey(ProjectPost, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.requestor} requested to join {self.post.title} (Status: {self.status})'
