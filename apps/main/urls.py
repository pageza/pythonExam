from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.create_user),
    url(r'^quotes$', views.success),
    url(r'^sessions$', views.log_in),
    url(r'^create$', views.create_quote),
    url(r'^user/(?P<id>\d+)$', views.user),
    url(r'^log_out$', views.log_out),
    url(r'^add/(?P<id>\d+)$', views.add),
    url(r'^remove/(?P<id>\d+)$', views.remove),
]
