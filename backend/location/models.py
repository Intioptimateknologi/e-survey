from django import db
from django.db import models

class provinsi(models.Model):
    provinsi = models.CharField(max_length=10)
    nama_provinsi = models.CharField(max_length=100)
    provinsi_singkat = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    latitude2 = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True)
    longitude2 = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    geom = models.JSONField(null=True)
    line_geom = models.JSONField(null=True)

    class Meta:
        managed = True
        ordering = ['-nama_provinsi', ]
        verbose_name = 'Provinsi'
        verbose_name_plural = 'Daftar Provinsi'

    def __str__(self):
        return f'{self.nama_provinsi.capitalize()}'

class kabupaten(models.Model):
    kabupaten = models.CharField(max_length=10)
    provinsi = models.ForeignKey(provinsi, on_delete=models.CASCADE, null=True, blank=True)
    nama_kabupaten = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    geom = models.JSONField(null=True)

    class Meta:
        managed = True
        ordering = ['nama_kabupaten', ]
        verbose_name = 'Kabupaten'
        verbose_name_plural = 'Daftar Kabupaten'

    def __str__(self):
        return str(self.nama_kabupaten)

class kecamatan(models.Model):
    kecamatan = models.CharField(max_length=10)
    kabupaten = models.ForeignKey(kabupaten, on_delete=models.CASCADE, null=True, blank=True)
    nama_kecamatan = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    geom = models.JSONField(null=True)

    class Meta:
        managed = True
        ordering = ['nama_kecamatan', ]
        verbose_name = 'Kecamatan'
        verbose_name_plural = 'Daftar Kecamatan'

    def __str__(self):
        return str(self.nama_kecamatan)

class desa(models.Model):
    wilayah = models.CharField(max_length=255)
    nama_desa = models.CharField(max_length=100)
    nama_kecamatan = models.CharField(max_length=100)
    nama_kabupaten = models.CharField(max_length=100)
    nama_provinsi = models.CharField(max_length=100)
    desa = models.CharField(max_length=100)
    provinsi = models.ForeignKey(provinsi, on_delete=models.CASCADE)
    kabupaten = models.ForeignKey(kabupaten, on_delete=models.CASCADE)
    kecamatan = models.ForeignKey(kecamatan, on_delete=models.CASCADE)
    keterangan = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-id', ]
        verbose_name = 'Desa'
        verbose_name_plural = 'Daftar Desa'