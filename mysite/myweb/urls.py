from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home', views.home, name = 'home'),
    url(r'^search', views.search, name = 'search'),
    url(r'^list/(?P<page_id>[0-9]+)/$', views.listGet, name = 'list'),
    url(r'^list/good_id/(?P<good_id>MR-[0-9A-Z]+)/$', views.good, name = 'good')
]