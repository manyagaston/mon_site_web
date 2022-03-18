from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from django.urls import reverse_lazy

from .models import home

class groukamloginview(LoginView):
    template_name = 'login/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

class homelistview(ListView):
    model = home
    
    