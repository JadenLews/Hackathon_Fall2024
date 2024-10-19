from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/<str:username>/', views.portfolio_page, name='portfolio_page'),
    path('', views.home, name='home'),  # Example for your home page
    path('profile/', views.profile, name='profile'),
]
