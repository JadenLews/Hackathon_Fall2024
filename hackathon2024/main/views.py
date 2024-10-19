from django.shortcuts import render
from .models import ProjectPost
# Create your views here.
def portfolio_page(request):
    return render(request, "main/portfolio.html")

def home(request):
    # Fetch all posts from the database
    posts = ProjectPost.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, "main/home.html", context)