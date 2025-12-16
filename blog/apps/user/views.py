from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as LoginViewDjango, LogoutView as LogoutViewDjango
from django.contrib.auth.models import Group
from apps.user.forms import LoginForm, RegisterForm
from django.urls import reverse_lazy

class UserProfileView(TemplateView):
    template_name = "user/user-profile.html"



class LoginView(LoginViewDjango):
    template_name = 'auth/auth-login.html'
    authenticcation_form = LoginForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        
        if next_url:
            return next_url
        
        return reverse_lazy("home")
    

class RegisterView(CreateView): 
    template_name = 'auth/auth-register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form) 

        registrado_group = Group.objects.get(name="registrado")
        self.object.groups.add(registrado_group)

        return response


class LogoutView(LogoutViewDjango):
    def get_success_url(self):
        next_url = self.request.GET.get('next')

        if next_url:
            return next_url
        
        return reverse_lazy('home')