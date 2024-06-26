# Generated by Django 5.0.3 on 2024-05-07 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Penyewaan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nomor_telepon', models.CharField(max_length=20)),
                ('merek', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('tahun', models.IntegerField()),
                ('tanggal_sewa', models.DateField()),
                ('tanggal_pengembalian', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
