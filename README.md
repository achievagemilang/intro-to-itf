# Fuki Store - Week 1

## Daftar Isi
1. [Pengenalan Client Side dan Server Side](#1-init-django-project)
2. Hands-on projek FUKI Store
3. Django urls (url params)
4. Functional Based views
5. Interact with Database



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