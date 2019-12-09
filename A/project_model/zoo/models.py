from django.db import models

# Create your models here.
class Hewan(models.Model):
    nama = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    berat = models.IntegerField(default=0)
    umur = models.IntegerField(default=0)

    def __str__(self):
        return self.nama+" ({})".format(self.species)

class Kandang(models.Model):
    nama = models.CharField(max_length=50)
    isi_kandang = models.CharField(max_length=200)
    luas_kandang = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nama+" (Isi: {})".format(self.isi_kandang)

class Penjaga(models.Model):
    nama = models.CharField(max_length=50)
    nomor_telepon = models.CharField(max_length=15)
    jadwal_jaga = models.DateTimeField("Jadwal Jaga")
    
    def __str__(self):
        return self.nama+" (Jadwal jaga: {})".format(self.jadwal_jaga)
    
class Pengunjung(models.Model):
    nama = models.CharField(max_length=50)
    nomor_telepon = models.CharField(max_length=15)
    hari_berkunjung = models.DateField("Hari Berkunjung")

    def __str__(self):
        return self.nama+" (Kunjungan: {})".format(self.hari_berkunjung)