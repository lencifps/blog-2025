from django.urls import path
import apps.user.views as views 

app_name = 'user'


urlpatterns = [
    path('user/profile', views.UserProfileView.as_view(), name='user-profile'),
    path('auth/login', views.LoginView.as_view(), name='auth-login'),
    path('auth/register', views.RegisterView.as_view(), name='auth-register'),
]