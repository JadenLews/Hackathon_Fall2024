from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('portfolio/<str:username>/', views.portfolio_page, name='portfolio_page'),
    # path('', views.home, name='home'),  
    # path('profile/', views.profile, name='profile'),
    path("", views.home, name="home"),
    path("templates/main/login.html", views.login, name="login"),
    path("templates/main/signup.html", views.signup, name="signup"),
    path("templates/main/login/", views.login_view, name="login_view"),
    path("templates/main/signup/", views.signup_view, name="signup_view"),
]
