# forms produk

from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from .models import Produk, Model, Variant, Material

class FormProduk(ModelForm):
    class Meta:
        model = Produk
        fields = '__all__'

    widgets = {
        'nama_produk' : forms.TextInput({'class':'form-control'}),
    }

class FormModel(ModelForm):
    class Meta:
        model = Model
        fields = '__all__'

    widgets = {
        'nama_model' : forms.TextInput({'class':'form-control'}),
        'produk_id' : forms.Select({'class':'forms-control'}),

    }

class FormVariant(ModelForm):
    class Meta:
        model = Variant
        fields = '__all__'

    widgets = {
        'nama_variant' : forms.TextInput({'class':'form-control'}),
        'nama_atribut' : forms.TextInput({'class':'form-control'}),
        'nilai_atribut' : forms.TextInput({'class':'form-control'}),
        'model_id' : forms.Select({'class':'forms-control'}),
    }

class FormMaterial(ModelForm):
    class Meta:
        model = Material
        fields = '__all__'

    widgets = {
        'nama_material' : forms.TextInput({'class':'form-control'}),
        'nama_supplier' : forms.TextInput({'class':'form-control'}),
        'penyusun_produk' : forms.TextInput({'class':'form-control'}),
        'is_diubah' : forms.BooleanField(required=False),
        'tanggal_material_dibuah' : forms.DateField({'class':'form-control'}),
        'keterangan' : forms.TextInput({'class':'form-control'}),
    }