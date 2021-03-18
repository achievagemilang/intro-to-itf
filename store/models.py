from django.db import models

# Create your models here.

class Penjual(models.Model):
    nama_depan = models.CharField(max_length=30)
    nama_belakang = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.nama_depan, self.nama_belakang)

class Barang(models.Model):
    nama_barang = models.CharField(max_length=100)
    harga_barang = models.DecimalField(max_digits=10, decimal_places=0)
    deskripsi_barang = models.CharField(max_length=300, default=None)
    penjual = models.ForeignKey(Penjual, default=1,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="img/",default='img/default.png')
    

    def __str__(self):
        return self.nama_barang