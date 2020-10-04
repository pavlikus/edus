"""edus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

from .views import CourseCreateView, CourseDeleteView, CourseEditView, CourseDetailView, CoursesListView


urlpatterns = [
    path('', CoursesListView.as_view(), name='courses'),
    path('add/', login_required(CourseCreateView.as_view(), login_url='/login/'), name='course_add'),
    path('<slug>/', CourseDetailView.as_view(), name='course'),
    path('<slug>/edit/', login_required(CourseEditView.as_view(), login_url='/login/'), name='course_edit'),
    path('<slug>/delete/', login_required(CourseDeleteView.as_view(), login_url='/login/'), name='course_delete')  
]
