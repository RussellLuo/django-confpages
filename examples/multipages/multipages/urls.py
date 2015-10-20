"""multipages URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

# Added for confpages
from django.views.generic.base import RedirectView
from confpages.views import ConfPages
from multipages.loaders import loader_a, loader_b


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Added for confpages
    url(r'^a/$', RedirectView.as_view(url='/a/index/'),
        name='confpages-a-index'),
    url(r'^a/(?P<name>\w+)/$', ConfPages.as_view(page_loader=loader_a),
        name='confpages-a-detail'),
    url(r'^b/$', RedirectView.as_view(url='/b/index/'),
        name='confpages-b-index'),
    url(r'^b/(?P<name>\w+)/$', ConfPages.as_view(page_loader=loader_b),
        name='confpages-b-detail'),
]
