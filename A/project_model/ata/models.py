from django.db import models

# Create your models here.
class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length=50)
    nomor_telepon = models.CharField(max_length=15)
    bidang = models.CharField(max_length=20)

    def __str__(self):
        return self.nama_lengkap+" ({})".format(self.bidang)
    
class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length=50)
    nomor_telepon = models.CharField(max_length=15)
    nomor_absen = models.IntegerField(default=1)
    nilai_rerata = models.FloatField(default=0.0)

    def __str__(self):
        return self.nama_lengkap+" ({})".format(self.nomor_absen)
    
class MataPelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=50)
    jadwal_dimulai = models.DateTimeField("jadwal_dimulai")
    jadwal_berakhir = models.DateTimeField("jadwal_berakhir")

    def __str__(self):
        return self.nama_pelajaran+" ({} - {})".format(self.jadwal_dimulai, self.jadwal_berakhir)
    
class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length=50)
    nomor_telepon = models.CharField(max_length=15)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_lengkap+" ({})".format(self.mata_pelajaran.nama_pelajaran)

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length=50)
    banyak_soal = models.IntegerField(default=1)
    bobot_nilai = models.IntegerField(default=100)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_challenge+" (Bobot: {}%)".format(self.bobot_nilai)

class LiveCode(models.Model):
    nama_live_code = models.CharField(max_length=50)
    banyak_soal = models.IntegerField(default=1)
    bobot_nilai = models.IntegerField(default=100)
    tanggal_pelaksanaan = models.DateField("Tanggal Pelaksanaan")
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_live_code+" ({})".format(self.tanggal_pelaksanaan)