from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addcourse$', views.addcourse),
    url(r'confirm/(?P<id>\d+)$', views.confirm),
    url(r'confirmed$', views.delete),
]
