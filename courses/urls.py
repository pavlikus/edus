from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

from .views import CourseCreateView, CourseDeleteView, CourseEditView, CourseDetailView
from .views import CoursesView, CoursesListView


urlpatterns = [
    path('', CoursesView.as_view(), name='courses'),
    path('add/', login_required(CourseCreateView.as_view(), login_url='/login/'), name='course_add'),
    path('<slug>/', CourseDetailView.as_view(), name='course'),
    path('<slug>/edit/', login_required(CourseEditView.as_view(), login_url='/login/'), name='course_edit'),
    path('<slug>/delete/', login_required(CourseDeleteView.as_view(), login_url='/login/'), name='course_delete')  
]
