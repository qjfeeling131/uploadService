from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from documentService import views

urlpatterns = [
    url(r'^fileUpload', views.UploadFile.as_view()),
    url(r'^getDigitalInformations',views.getDocumentInformation.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
