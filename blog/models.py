from django.db import models

class Kullanici(models.Model):
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    email = models.EmailField()
    sifre = models.CharField(max_length=100)
    telefon = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.ad} {self.soyad}"



