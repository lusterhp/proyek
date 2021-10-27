from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from produk.models import *

# Create your models here.
class LapakKerja(models.Model):
    nama_lapak = models.CharField(max_length=50)
    availabilitas = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.nama_lapak)

class KodePeralatan(models.Model):
    kode_alat = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.kode_alat)

class PeralatanKerja(models.Model):
    nama_alat = models.CharField(max_length=50)
    kodealat_id = models.ForeignKey(KodePeralatan, on_delete=CASCADE)
    availabilitas = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.nama_alat)
