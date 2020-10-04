from django.views.generic import CreateView, DetailView, DeleteView
from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy

from .models import Course


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
    fields = '__all__'


class CourseDeleteView(DeleteView):

    model = Course
    success_url = reverse_lazy('courses')


class CourseEditView(UpdateView):

    context_object_name = 'course'
    fields = 'name', 'description'
    model = Course
    template_name = 'courses/course_edit.html'
