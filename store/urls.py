from . import views
from django.urls import path

# to do : menambahkan url untuk tambah-barang dan tambah-penjual
urlpatterns = [
    path('', views.index, name='index'),
]
