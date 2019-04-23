from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'index/$', views.index),
    url(r'single/(\d+)/$', views.single),
    url(r'comment/(\d+)/$', views.comment)
]