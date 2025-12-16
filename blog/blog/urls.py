from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings

# Vistas simples (temporales hasta que crees las vistas reales)
urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Páginas estáticas
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    
    # Blog (temporales - luego reemplazarás con vistas reales)
    path('blog/', TemplateView.as_view(template_name='blog/post_list.html'), name='post_list'),
    path('blog/<slug:slug>/', TemplateView.as_view(template_name='blog/post_detail.html'), name='post_detail'),
    path('blog/category/<slug:slug>/', TemplateView.as_view(template_name='blog/post_list.html'), name='category_posts'),
    path('blog/create/', TemplateView.as_view(template_name='blog/post_form.html'), name='create_post'),
    
    # Autenticación (temporales)
    path('login/', TemplateView.as_view(template_name='users/login.html'), name='login'),
    path('register/', TemplateView.as_view(template_name='users/register.html'), name='register'),
    path('logout/', TemplateView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', TemplateView.as_view(template_name='users/profile.html'), name='profile'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
