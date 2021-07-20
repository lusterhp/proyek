from django.db import models
from django.db.models.base import Model

# Create your models here.
class Pesanan(models.Model):
    kebutuhan_alat = models.CharField(max_length=20)
    kebutuhan_lapak = models.IntegerField(null=True)
    kebutuhan_group = models.IntegerField(null=True)
    waktu_mulai = models.DateTimeField()

    def __str__(self):
        return "{}".format(self.waktu_mulai)

class AlatLas(models.Model):
    availabilitas = models.BooleanField()
    timeline_alat = models.DateTimeField()

class CatElektroplating(models.Model):
    availabilitas = models.BooleanField()
    timeline_alat = models.DateTimeField()

class KerjaBangku(models.Model):
    availabilitas = models.BooleanField()
    timeline_alat = models.DateTimeField()

class MesinCNC(models.Model):
    availabilitas = models.BooleanField()
    timeline_alat = models.DateTimeField()

class LapakUtara(models.Model):
    timeline_lapak = models.DateTimeField()
    timeline_group01 = models.DateTimeField()
    timeline_group02 = models.DateTimeField()
    timeline_group03 = models.DateTimeField()

class LapakSelatan(models.Model):
    timeline_lapak = models.DateTimeField()
    timeline_group01 = models.DateTimeField()
    timeline_group02 = models.DateTimeField()
    timeline_group03 = models.DateTimeField()

class GroupKerja01(models.Model):
    availabilitas = models.BooleanField()
    timeline_group01 = models.DateTimeField()
    AlatLas_id = models.ForeignKey(AlatLas, on_delete=models.CASCADE, null=True)
    CatElektroplating_id = models.ForeignKey(CatElektroplating, on_delete=models.CASCADE, null=True)
    KerjaBangku_id = models.ForeignKey(KerjaBangku, on_delete=models.CASCADE, null=True)
    MesinCNC_id = models.ForeignKey(MesinCNC, on_delete=models.CASCADE, null=True)
    LapakUtara_id = models.ForeignKey(LapakUtara, on_delete=models.CASCADE, null=True)
    LapakSelatan_id = models.ForeignKey(LapakSelatan, on_delete=models.CASCADE, null=True)

class GroupKerja02(models.Model):
    availabilitas = models.BooleanField()
    timeline_group02 = models.DateTimeField()
    AlatLas_id = models.ForeignKey(AlatLas, on_delete=models.CASCADE, null=True)
    CatElektroplating_id = models.ForeignKey(CatElektroplating, on_delete=models.CASCADE, null=True)
    KerjaBangku_id = models.ForeignKey(KerjaBangku, on_delete=models.CASCADE, null=True)
    MesinCNC_id = models.ForeignKey(MesinCNC, on_delete=models.CASCADE, null=True)
    LapakUtara_id = models.ForeignKey(LapakUtara, on_delete=models.CASCADE, null=True)
    LapakSelatan_id = models.ForeignKey(LapakSelatan, on_delete=models.CASCADE, null=True)

class GroupKerja03(models.Model):
    availabilitas = models.BooleanField()
    timeline_group03 = models.DateTimeField()
    AlatLas_id = models.ForeignKey(AlatLas, on_delete=models.CASCADE, null=True)
    CatElektroplating_id = models.ForeignKey(CatElektroplating, on_delete=models.CASCADE, null=True)
    KerjaBangku_id = models.ForeignKey(KerjaBangku, on_delete=models.CASCADE, null=True)
    MesinCNC_id = models.ForeignKey(MesinCNC, on_delete=models.CASCADE, null=True)
    LapakUtara_id = models.ForeignKey(LapakUtara, on_delete=models.CASCADE, null=True)
    LapakSelatan_id = models.ForeignKey(LapakSelatan, on_delete=models.CASCADE, null=True)

class KoordinatorGroup(models.Model):
    group_available = models.CharField(max_length=20)
    timeline_kosong = models.DateTimeField()