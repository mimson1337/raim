"""
URL configuration for adnotation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import save_annotation

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index,  name='index'),
    path('photo-list/', views.photo_list, name='photo_list'),
    path('save_annotation/', save_annotation, name='save_annotation'),
    # path('upload/', views.index),  # Dodaj ścieżkę do widoku przesyłania zdjęć
    # path('upload/upload/', RedirectView.as_view(url='/upload/')),  # przekieruj /upload/upload na /upload
    # path('save_image/', views.save_image, name='save_image'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL,
#                               document_root=settings.MEDIA_ROOT)


