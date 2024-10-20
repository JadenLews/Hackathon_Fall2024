from django.shortcuts import render, redirect, get_object_or_404
from .models import ProjectPost
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile, ProjectPost
from .models import Profile
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth import get_user_model
from .managers import CustomUserManager
import random
from django.db.models import Avg
from django.http import HttpResponseNotFound
from django.utils import timezone
from django.http import HttpResponse


def login(request):
    return render(request, "main/login.html")

def signup(request):
    return render(request, "main/signup.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get(
            "username"
        )  # Assuming your login form has a field named 'username'
        password = request.POST.get(
            "password"
        )  # Assuming your login form has a field named 'password'

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            # User is authenticated, log them in
            auth_login(request, user)
            return redirect("home")  # Redirect to home page after successful login
        else:
            # Authentication failed
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, "main/login.html")

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        if not email.endswith("@clarku.edu"):
            messages.error(request, "Must use a Clark email address.")
            return redirect("signup")

        User = get_user_model()
        if User.objects.filter(username=username).exists():
            messages.error(
                request, "Username already exists. Please choose a different username."
            )
            return redirect("signup")
        if User.objects.filter(email=email).exists():
            messages.error(
                request, "Email already exists. Please use a different email address."
            )
            return redirect("signup")

        user_manager = CustomUserManager()
        new_user = user_manager.create_user(
            username=username, email=email, password=password
        )

        return redirect("login")

    return render(request, "main/signup.html")
# Create your views here.
@login_required
def portfolio_page(request):
    # Ensure the user has a profile
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    # Fetch the user's posts if applicable
    user_posts = ProjectPost.objects.filter(user=request.user)

    context = {
        'user': request.user,
        'profile': request.user.profile,
        'posts': user_posts,
    }

    return render(request, "main/portfolio.html", context)


from django.shortcuts import render
from .models import ProjectPost, Profile

def home(request):
    # Fetch all posts with related user profiles
    posts = ProjectPost.objects.all()
    
    # Create a list of posts with corresponding user profiles
    posts_with_profiles = []
    for post in posts:
        try:
            profile = Profile.objects.get(user=post.user)  # Get profile for each post's user
        except Profile.DoesNotExist:
            profile = None  # In case the user has no profile

        posts_with_profiles.append({
            'post': post,
            'profile_image': profile.profile_image.url if profile and profile.profile_image else None
        })

    context = {
        'posts': posts_with_profiles,
    }
    return render(request, "main/home.html", context)




@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('/portfolio')  # Redirect to portfolio page after saving
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'profile.html', context)

@login_required
def save_social_links(request):
    profile = request.user.profile  # Assuming a OneToOne relationship between User and Profile

    if request.method == 'POST':
        # Get data from the form
        profile.linkedin = request.POST.get('linkedin', '')
        profile.git = request.POST.get('github', '')
        profile.choice_site = request.POST.get('twitter', '')

        # Save the updated profile data
        profile.save()

        return redirect('profile')  # Redirect to the profile page

    return render(request, 'portfolio.html', {'profile': profile})