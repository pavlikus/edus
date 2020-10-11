from datetime import datetime

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from courses.models import CourseStream


class Index(TemplateView):

    http_method_names = ['get']
    template_name = 'index.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['courses'] = CourseStream.objects.filter(date_start__gte=datetime.now())
        return context
    

class AccountLoginView(LoginView):

    redirect_authenticated_user = True
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('index')


class AccountLogoutView(LogoutView):
    
    def get_next_page(self):
        return reverse_lazy('index')
