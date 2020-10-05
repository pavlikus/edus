from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.urls import reverse_lazy


class Index(TemplateView):
    
    http_method_names = ['get']
    template_name = 'index.html'
    

class AccountLoginView(LoginView):

    redirect_authenticated_user = True
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('index')


class AccountLogoutView(LogoutView):
    
    def get_next_page(self):
        return reverse_lazy('index')
