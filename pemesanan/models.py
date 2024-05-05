from django.db import models

class Penyewaan(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    nomor_telepon = models.CharField(max_length=20)
    merek = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    tahun = models.IntegerField()
    tanggal_sewa = models.DateField()
    tanggal_pengembalian = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nama
    
    
