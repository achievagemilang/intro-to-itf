from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Penjual,Barang
from .forms import tambahBarangForm, tambahPenjualForm


# Create your views here.
def index(request):
	list_barang = Barang.objects.all()
	

	#list_penjual = Penjual.objects.all()
	#data_penjual = []
	#for penjual in list_penjual:
	#	list_barang = Barang.objects.filters(penjual=penjual)
	#	data_barang = []
	#	for barang in list_barang:
	#		data_barang.append(barang)
	#	data_penjual.append((penjual,data_barang)) 
	#context={'data_penjual': data_penjual}


	context={ "list_barang":list_barang}
	return render(request,"store/index.html", context)

def tambah_barang(request):
	
	if (request.method == 'POST') :
		form = tambahBarangForm(request.POST,request.FILES)

		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = tambahBarangForm()
	context = {'form': form}

	return render(request,"store/tambah_barang.html",context)

def tambah_penjual(request):
	form = tambahPenjualForm()
	if(form.is_valid and request.method == 'POST'):
		form = tambahPenjualForm(request.POST)
		form.save()
		return redirect('/')
	context ={'form' : form}
	return render(request,"store/tambah_penjual.html",context)