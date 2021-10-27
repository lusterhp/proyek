from django.contrib import admin

# Register your models here.
from produk.models import *

admin.site.register(Produk);
admin.site.register(Model);
admin.site.register(Variant);
admin.site.register(Material);
