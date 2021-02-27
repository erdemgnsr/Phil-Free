from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "lessons"

urlpatterns = [
    path("", views.index, name = "index"),
    path("lesson/<int:id>", views.lesson, name = "lesson"),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)