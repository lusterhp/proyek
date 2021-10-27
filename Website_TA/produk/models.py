from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Produk(models.Model):
    nama_produk = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.nama_produk)

class Model(models.Model):
    nama_model = models.CharField(max_length=255)
    produk_id = models.ForeignKey(Produk, on_delete=CASCADE)

    def __str__(self):
        return "{}".format(self.nama_model)

class Variant(models.Model):
    nama_variant = models.CharField(max_length=255)
    nama_atribut = models.CharField(max_length=255)
    nilai_atribut = models.CharField(max_length=255)
    model_id = models.ForeignKey(Model, on_delete=CASCADE)

    def __str__(self):
        return "{}".format(self.nama_variant)

class Material(models.Model):
    nama_material = models.CharField(max_length=255)
    nama_supplier = models.CharField(max_length=255)
    penyusun_produk = models.CharField(max_length=255)
    is_diubah = models.BooleanField(default=False)
    tanggal_material_diubah = models.DateField(blank=True, null=True)
    keterangan = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.nama_material)
