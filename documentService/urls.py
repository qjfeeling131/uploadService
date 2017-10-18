from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from documentService import views


urlpatterns = [
    url(r'^api/handleFiles', views.HandleFiles.as_view()),
    url(r'^api/digitalAsset/',views.digitalAssets.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
