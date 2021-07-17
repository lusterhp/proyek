# urls order

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^daftar/$', views.daftar),
    url(r'^$', views.order),
    url(r'^form/$', views.form),
]
