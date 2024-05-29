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
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import save_annotation

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index,  name='index'),
    path('photo-list/', views.photo_list, name='photo_list'),
    path('save_annotation/', save_annotation, name='save_annotation'),
    path('upload_annotations/', views.upload_annotations, name='upload_annotations'),
    path('edit_annotations/<int:image_id>/', views.edit_annotations, name='edit_annotations'),
    path('upload_annotations/', views.upload_annotations, name='upload_annotations'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


