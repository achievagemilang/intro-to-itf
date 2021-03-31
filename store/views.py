from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Penjual,Barang
from .forms import tambahBarangForm, tambahPenjualForm


# Create your views here.
# To Do : Create a function for showing the index, submit form for tambah_barang, and submit form fortambah_penjual