from django import forms
from django.views.generic import CreateView, DetailView, DeleteView
from django.views.generic import TemplateView
from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy

from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

from .models import Course
from .forms import CourseCreateForm
from .serializers import CourseListSerializer


class CoursesView(TemplateView):

    template_name = 'courses/index.html'


class CoursesListView(ListView):

    context_object_name = 'courses'
    model = Course
    template_name = 'courses/index.html'


class CourseDetailView(DetailView):

    context_object_name = 'course'
    model = Course
    template_name = 'courses/course.html'


class CourseCreateView(CreateView):

    model = Course
    form_class = CourseCreateForm


class CourseDeleteView(DeleteView):

    model = Course
    success_url = reverse_lazy('courses')


class CourseEditView(UpdateView):

    context_object_name = 'course'
    fields = 'name', 'description'
    model = Course
    template_name = 'courses/course_edit.html'


class CourseAPIListView(ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
