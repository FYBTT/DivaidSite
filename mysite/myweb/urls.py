from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home', views.home, name = 'home'),
    url(r'^list/query/(?P<country>[0-9]+)/((?P<query>[&\s0-9A-Za-z/-]+))/$', views.listPage, name = 'listPage'),
    url(r'^list/AjaxQuery/((?P<query>[&\s0-9A-Za-z/-]+))/(?P<country>[0-9]+)/(?P<page_id>[0-9]+)/$', views.listAjaxGet, name = 'listAjaxGet'),
    url(r'^list/good_id/(?P<good_id>[&\s0-9A-Za-z/-]+)/$', views.good, name = 'good')
]

handler404=views.page_not_found