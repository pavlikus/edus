from django.views.generic import DetailView, ListView

from .models import Teacher


class TeachersListView(ListView):

    context_object_name = 'teachers'
    model = Teacher
    template_name = 'members/teachers.html'

    
class TeacherDetailView(DetailView):

    context_object_name = 'teacher'
    model = Teacher
    template_name = 'members/teacher.html'
