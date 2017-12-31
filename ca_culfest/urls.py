"""ca_culfest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from home import views as home_views
from django.conf import settings
from django.views.static import serve as staticserve
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', home_views.index, name="index"),
    url(r'^register/$', home_views.update_profile, name="register"),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', home_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^home/', include('home.urls')),
] + [url(r'^media/(?P<path>.*)$', staticserve, {'document_root': settings.MEDIA_ROOT, })]
