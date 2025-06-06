"""
URL configuration for hackathon2024 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views as main_views
from django.shortcuts import redirect

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", main_views.home, name="home"),
    path("main/", include("main.urls")),
    path("", lambda req: redirect('home/')),
    path("profile/", main_views.profile, name="profile"), 
    path("portfolio2/", main_views.portfolio_page, name="profile"), 
    path('create-project/', main_views.create_project_post, name='create-project'),
    path('portfolio/<str:username>/', main_views.portfolio_page2, name='portfolio'),
    path('request-to-join/<int:post_id>/', main_views.request_to_join, name='request_to_join'),
    path('accept-request/<int:notification_id>/', main_views.accept_request, name='accept_request'),
    path('reject-request/<int:notification_id>/', main_views.reject_request, name='reject_request'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)