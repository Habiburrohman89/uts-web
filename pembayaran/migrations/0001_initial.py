# Generated by Django 5.0.3 on 2024-05-07 08:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pemesanan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pembayaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah', models.DecimalField(decimal_places=2, max_digits=10)),
                ('merek', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('tahun', models.IntegerField()),
                ('metode_pembayaran', models.CharField(max_length=100)),
                ('tanggal_pembayaran', models.DateTimeField(auto_now_add=True)),
                ('penyewa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pembayaran', to='pemesanan.penyewaan')),
            ],
        ),
    ]
