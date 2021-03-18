from django import forms
from store.models import Penjual
from store.models import Barang
from django.db import migrations, models

 

class tambahBarangForm(forms.ModelForm):
    photo = forms.ImageField(required=False)
    class Meta:
        model = Barang
        fields = "__all__"
    #penjual = forms.ModelMultipleChoiceField(queryset=Penjual.objects.all(),
    #										 widget=forms.CheckboxSelectMultiple(
    #										 attrs={'class':'browser-default',
    #										 		'id':'select'}),
    #										 required=True,)
    #penjual = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[(c.pk, c.nama_depan) for c in Penjual.objects.all()])
    #penjual = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=DEMO_CHOICES)

class tambahPenjualForm(forms.ModelForm):

	class Meta:
		model = Penjual
		fields = "__all__"

# course = forms.MultipleChoiceField(
#         widget=forms.CheckboxSelectMultiple,
#         choices=[(c.pk, c.name) for c in Course.objects.all()],
#     ) 