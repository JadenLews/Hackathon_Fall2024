from django.shortcuts import render, redirect
from .models import ProjectPost
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile
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


@login_required
def profile(request):
    # Ensure the user has a profile
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'profile.html', context)