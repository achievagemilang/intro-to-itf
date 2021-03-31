from . import views
from django.urls import path

# To Do : Add routing url for 'Tambah Barang' and 'Tambah Penjual'
urlpatterns = [
    path('', views.index, name='index'),
]
