from django.db import models

# Create your models here.
class Dokter(models.Model):
    nama = models.CharField(max_length=50)
    nomor_telepon = models.CharField(max_length=15)
    bidang = models.CharField(max_length=20)
    jadwal_praktek = models.DateTimeField("jadwal_praktek")

    def __str__(self):
        return self.nama+" ({})".format(self.bidang)

class Pasien(models.Model):
    nama = models.CharField(max_length=50)
    nomor_telepon = models.CharField(max_length=15)
    alamat = models.CharField(max_length=200)
    keluhan = models.CharField(max_length=200)

    def __str__(self):
        return self.nama+" ({})".format(self.nomor_telepon)

class Obat(models.Model):
    nama_obat = models.CharField(max_length=50)
    kandungan = models.CharField(max_length=100)
    khasiat = models.CharField(max_length=200)

    def __str__(self):
        return self.nama_obat+" ({})".format(self.kandungan)

class Resep(models.Model):
    nama = models.ForeignKey(Pasien, on_delete=models.CASCADE)
    kumpulan_obat = models.ForeignKey(Obat, on_delete=models.CASCADE)
    total_harga = models.IntegerField(default=0)

    def __str__(self):
        return "Sdr. "+self.nama.nama+" (Rp{})".format(self.total_harga)