from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Penjual,Barang
from .forms import tambahBarangForm, tambahPenjualForm


# Create your views here.
# to do : membuat fungsi untuk index, tambah_barang, dan tambah_penjual