from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('tambah-barang', views.tambah_barang, name="tambah_barang"),
    path('tambah-penjual', views.tambah_penjual, name="tambah_penjual")
]
