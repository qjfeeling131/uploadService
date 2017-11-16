from django.conf.urls import url
from documentService import views

urlpatterns = [
   url(r'^api/handleFiles', views.HandleFiles.as_view()),
]