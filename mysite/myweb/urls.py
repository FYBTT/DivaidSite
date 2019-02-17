from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home', views.home, name = 'home'),
    url(r'^list/query/((?P<query>[0-9A-Za-z/-]+))/$', views.listPage, name = 'listPage'),
    url(r'^list/AjaxQuery/((?P<query>[0-9A-Za-z/-]+))/(?P<page_id>[0-9]+)/$', views.listAjaxGet, name = 'listAjaxGet'),
    url(r'^list/good_id/(?P<good_id>MR-[0-9A-Za-z]+)/$', views.good, name = 'good')
]