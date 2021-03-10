from django.urls import path
from . import views
from django.conf.urls import url
from .views import File_for_view
urlpatterns = [
    path("", File_for_view.as_view(), name='file-upload'),
    
    
]