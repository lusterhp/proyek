from datetime import datetime
from django.db import models
from produk.models import *
from projectshop.models import *

# Create your models here.

class ProsesKerja(models.Model):
    nama_proses = models.CharField(max_length=255)
    material_id = models.ForeignKey(Material, on_delete=CASCADE, blank=True, null=True)
    peralatankerja_id = models.ForeignKey(PeralatanKerja, on_delete=CASCADE, blank=True, null=True)
    waktu_mulai = models.DateTimeField(null=False, blank=False)
    waktu_selesai = models.DateTimeField(null=False, blank=False)
    produk_id = models.ForeignKey(Produk, on_delete=CASCADE)
    lapakkerja_id = models.ForeignKey(LapakKerja, on_delete=CASCADE)

    def __str__(self):
        return "{}".format(self.nama_proses)
