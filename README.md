# Fuki Store - Week 1

## Daftar Isi
- [Fuki Store - Week 1](#fuki-store---week-1)
  - [Daftar Isi](#daftar-isi)
  - [1. Init Django Project](#1-init-django-project)
  - [2. Membuat Views Pada Aplikasi `store`](#2-membuat-views-pada-aplikasi-store)
  - [3. Membuat Urls pada Django](#3-membuat-urls-pada-django)
  - [4. Berkenalan dengan Database (Django Models)](#4-berkenalan-dengan-database-django-models)



## 1. Init Django Project
Anda dapat mengetahui Django diinstal dan versi mana dengan menjalankan perintah berikut dalam prompt shell
```shell
> python -m django --version
```
Dari Terminal, cd ke direktori tempat Anda ingin menyimpan kode, lalu jalankan perintah berikut:
```shell
> django-admin startproject fukistore .
```
**notasi titik(.) pada akhir command artinya meletakkan folder proyek di lokasi direktori saat ini.** <br>

struktur folder saat ini
```
|- fukistore         <-- folder root project
|  |- __init.py
|  |- asgi.py
|  |- settings.py
|  |- urls.py
|  |- wsgi.py
|- manage.py
```
`setelah membuat project kita dapat membuat virtual environment`
```shell
> python -m venv env
> env\Scripts\activate     <-- activating virtualenv
> pip install django
```
`*OPTIONAL Anda dapat menamainya dengan nama lain seperti`
```shell
> python -m venv kronos
```

selanjutnya untuk membuat sebuah aplikasi pada projek **fukistore** dengan menuliskan command
```shell
> python manage.py startapp store
```
Perintah diatas akan membuat directory aplikasi **store**.
```
|- fukistore         <-- folder root project
|  |- __init.py
|  |- asgi.py
|  |- settings.py
|  |- urls.py
|  |- wsgi.py
|- store             <-- folder application
|  |- migrations
|  |  |- __init.py
|  |- __init.py
|  |- admin.py
|  |- apps.py
|  |- models.py
|  |- tests.py
|  |- views.py
|- manage.py
```
dan daftarkan application **store** pada file `fukistore/settings.py`.
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store', <--
]
```


## 2. Membuat Views Pada Aplikasi `store`
untuk menampilkan halaman utama, pada directory **store/views.py** tambahkan kode berikut:
```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "store/index.html")
```
buatlah file `index.html` pada directory `store/templates/store/index.html` dan isi dengan html sebagai berikut
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Selamat Datang di FukiStore 🎉</h1>
</body>
</html>
```
dengan begitu function `index` akan me-return tempalate `index.html`. tetapi untuk saat ini kita belum bisa mengaksesnya melalui url. selanjutnya akan dijelaskan bagaimana cara membuat urls.

## 3. Membuat Urls pada Django
Untuk membuat URL configurasi di direktori `store`, buat file bernama urls.py. Direktori sekarang akan seperti <br>

```
|- store             
|  |- migrations
|  |  |- __init.py
|  |- __init.py
|  |- admin.py
|  |- apps.py
|  |- models.py
|  |- tests.py
|  |- urls.py    <-- file baru
|  |- views.py
```
Pada file `urls.py` buatlah kode berikut
```python

from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
]
```
langkah selanjutnya kita harus mengarahkan url pada root project (`fukistore/urls.py`) sebagai berikut 
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('store.urls')),
    path('admin/', admin.site.urls),
]
```
kode __`path('', include('store.urls'))`__ artinya dari meng-include url configurasi milik `store/urls.py` kepada url `<domain.com>/` dan `<domain.com>/admin` akan mengarah ke halaman admin.

setelah itu silahkan akses aplikasi `store` dengan
```shell
> python manage.py migration
> python manage.py runserver
```
akses url [localhost](http://127.0.0.1:8000/) dan akan tertampil halaman aplikasi kita seperti berikut <br>
![localhost](https://i.ibb.co/mF9JVv3/itf.png)


## 4. Berkenalan dengan Database (Django Models)
* Django Models
  * [Membuat Class pada `models.py`](#membuat-class-pada-homepagemodelspy)
  * [Mendaftarkan Class pada `admin.py`](#mendaftarkan-class-pada-homepageadminpy)
  * [Django CRUD (Create, Read, Update, Delete)](#Django-CRUD)
    * [Membuat Objek baru](#membuat-object-dari-model-yang-sudah-dibuat)
    * [Melihat Objek](#melihat-objek)
    * [Mengedit Objek](#mengedit-objek)
    * [Menghapus Objek](#menghapus-objek)
  * [Tabel Tipe Data](#tabel-tipe-data)
  * [Relationship Fields](#tabel-jenis-jenis-relationship-)

Membuat Class pada `store/models.py`
---
```python
from django.db import models

class Penjual(models.Model):
    nama_depan = models.CharField(max_length=30)
    nama_belakang = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.nama_depan, self.nama_belakang)
```
```python
class Barang(models.Model):
    nama_barang = models.CharField(max_length=100)
    harga_barang = models.DecimalField(max_digits=10, decimal_places=0)
    deskripsi_barang = models.CharField(max_length=300, default=None)
    penjual = models.ForeignKey(Penjual, default=1,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="img/",default='img/default.png')
    

    def __str__(self):
        return self.nama_barang
```

Table Penjual

| id | nama_depan    | nama_belakang       | email                 |
|----|---------------|---------------------|-----------------------|
| 1  | ucup          | surucup             |ucup.surucup@gmail.com |
| 2  | pucu          | pucurus             |pucu.pucurus@gmail.com |


Mendaftarkan Class pada `store/admin.py`
---
Untuk membuat model dalam admin Django, kita perlu memodifikasi `store/admin.py`. Buka `admin.py` di store dan masukkan kode berikut. Import model terkait dari `models.py` dan daftarkan ke antarmuka admin.

```python
from django.contrib import admin  
    
# Register your models here.  
from .models import Penjual, Barang  
    
admin.site.register(Penjual)  
admin.site.register(Barang)  
```

### Melihat models lewat shell
---
jangan lupa untuk memigrasi tabel yang sudah dibuat
```bash
python manage.py makemigrations
python manage.py migrate
```

membuka shell untuk project django
```bash
$ python manage.py shell
```
lalu akan ada tampilan seperti shell pada python

```bash
Python 3.6.8 (default, Jan 14 2019, 11:02:34)
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

import class yang sudah di buat tadi di dalam folder app
```python
>>> from app.models import Penjual
```

Membuat object dari model yang sudah dibuat
---
```python
>>> Penjual(nama_depan='ucup',nama_belakang='surucup', email='ucup.surucup@gmail.com').save()
>>> Penjual(nama_depan='pucu', nama_belakang='pucurus', email='pucu.pucurus@gmail.com').save()
```

Melihat objek
---
query class yang sudah dibuat 

```python
>>> myProfile.objects.all()
<QuerySet [<Penjual: Penjual object (1)>, <Penjual: Penjual object (2)>]>
```

Mengedit objek
---
```python
>>> obj1 = Penjual.objects.get(id=1) #username:coba
>>> obj1.username = "cobaEdited"
>>> obj1.save()
```

Menghapus objek
---
```python
>>> obj2 = Penjual.onjects.get(id=2)
>>> obj2.delete()
```

Tabel tipe data
---
macam - macam field django diambil dari https://www.geeksforgeeks.org/django-model-data-types-and-fields-list/
basic data types

| Field Name    | Description                                                                                                          |
|---------------|----------------------------------------------------------------------------------------------------------------------|
| BooleanField  | A true/false field.The default form widget for this field is a CheckboxInput.                                        |
| CharField     | It is a date, represented in Python by a datetime.date instance.                                                     |
| DateField     | A date, represented in Python by a datetime.date instance                                                            |
| DateTimeField | It is used for date and time, represented in Python by a datetime.datetime instance.                                 |
| EmailField    | It is a CharField that checks that the value is a valid email address.                                               |
| FileField     | It is a file-upload field.                                                                                           |
| ImageField    | It inherits all attributes and methods from FileField, but also validates that the uploaded object is a valid image. |
| TextField     | A large text field. The default form widget for this field is a Textarea.                                            |
more : https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types
relationship fields

Tabel jenis-jenis relationship 
---
| Field name      | Description                                                                                                                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ForeignKey      | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.                                                                          |
| ManyToManyField | A many-to-many relationship. Requires a positional argument: the class to which the model is related, which works exactly the same as it does for ForeignKey, including recursive and lazy relationships. |
| OneToOneField   | A one-to-one relationship. Conceptually, this is similar to a ForeignKey with unique=True, but the “reverse” side of the relation will directly return a single object.                                   |

more : https://docs.djangoproject.com/en/2.2/ref/models/fields/#module-django.db.models.fields.related
