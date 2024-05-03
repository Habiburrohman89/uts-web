from django.db import models

class pemesanan(models.Model):
    NAMA = models.CharField(max_length=30)
    TANGGAL_SEWA = models.DateField()
    MOBIL = models.CharField(max_length=30)
    BERAPA_HARI = models.CharField(max_length=30)


    def __str__(self):
        return self.id,self.NAMA
    
    
