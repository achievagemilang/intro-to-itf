# Generated by Django 3.1.7 on 2021-03-18 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='deskripsi_barang',
            field=models.CharField(default=None, max_length=300),
        ),
    ]