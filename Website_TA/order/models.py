from django.db import models

# Create your models here.
class Pesanan(models.Model):
    kebutuhan_mesin = models.CharField(max_length=20)
    kebutuhan_lapak = models.IntegerField(null=True)
    kebutuhan_group = models.IntegerField(null=True)
    waktu_mulai = models.DateTimeField()