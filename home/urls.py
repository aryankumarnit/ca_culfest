from django.conf.urls import url
from . import views
app_name = 'home'
urlpatterns = [
    url(r'^$', views.base, name="base"),
    url(r'^download$', views.download, name="download"),
    url(r'^uploadfile$', views.uploadfile, name="uploadfile"),
]
