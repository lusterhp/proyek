# forms projectshop

from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from .models import *

class FormLapak(ModelForm):
    class Meta:
        model = LapakKerja
        fields = '__all__'

    widgets = {
        'nama_lapak' : forms.TextInput({'class':'form-control'}),
        'availabilitas': forms.BooleanField(required=False),
    }

class FormKode(ModelForm):
    class Meta:
        model = KodePeralatan
        fields = '__all__'

    widgets = {
        'kode_alat' : forms.TextInput({'class':'form-control'}),
    }

class FormAlat(ModelForm):
    class Meta:
        model = PeralatanKerja
        fields = '__all__'

    widgets = {
        'nama_alat' : forms.TextInput({'class':'form-control'}),
        'kodealat_id' : forms.Select({'class':'form-control'}),
        'availabilitas': forms.BooleanField(required=False),
    }