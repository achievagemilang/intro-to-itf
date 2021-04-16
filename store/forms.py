from django import forms
from store.models import Penjual
from store.models import Barang
from django.db import migrations, models

 

class tambahBarangForm(forms.ModelForm):
    photo = forms.ImageField(required=False)
    class Meta:
        model = Barang
        fields = "__all__"

class tambahPenjualForm(forms.ModelForm):

	class Meta:
		model = Penjual
		fields = "__all__"

