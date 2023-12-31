# Generated by Django 3.1.7 on 2021-03-18 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Penjual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_depan', models.CharField(max_length=30)),
                ('nama_belakang', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_barang', models.CharField(max_length=100)),
                ('harga_barang', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deskripsi_barang', models.CharField(default=None, max_length=400)),
                ('photo', models.ImageField(default=None, upload_to='img/%y')),
                ('penjual', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.penjual')),
            ],
        ),
    ]
