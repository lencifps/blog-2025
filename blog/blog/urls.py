from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from blog.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'), 
    
    
    path('', include('apps.user.urls')),
    path('', include('apps.post.urls')),
]


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)