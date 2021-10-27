# urls projectshop

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tambah-asset/$', views.form),
    url(r'^tambah-lapak/$', views.form1),
    url(r'^tambah-kodealat/$', views.form2),
    url(r'^tambah-peralatan/$', views.form3),
    url(r'^$', views.asset),
]