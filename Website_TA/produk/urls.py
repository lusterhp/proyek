# urls produk

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tambah/$', views.tambah),
    url(r'^tambah-produk/$', views.produk),
    url(r'^tambah-model/$', views.model),
    url(r'^tambah-variant/$', views.variant),
    url(r'^tambah-material/$', views.material),
    url(r'^$', views.list),
]
