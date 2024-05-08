from django.db import models
from pemesanan.models import Penyewaan

class Pembayaran(models.Model):
    penyewa = models.ForeignKey(Penyewaan, related_name='pembayaran', on_delete=models.CASCADE)
    jumlah = models.DecimalField(max_digits=10, decimal_places=2)
    merek = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    tahun = models.IntegerField()
    metode_pembayaran = models.CharField(max_length=100)
    tanggal_pembayaran = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama

    
