from django.db import models

class pembayaran(models.Model):
    nama = models.CharField(max_length=50)
    berapa_hari = models.CharField(max_length=10)
    harga = models.CharField(max_length=10)


    def __str__(self):
        return self.nama
    
