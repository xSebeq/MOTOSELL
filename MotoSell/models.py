from django.db import models
from softdelete.models import SoftDeleteObject
from django.contrib.auth.models import User


class Car(SoftDeleteObject, models.Model):
    MOTOCYKL = "Motocykl"
    OSOBOWY = "Osobowy"
    CIEZAROWY = "Ciężarowy"
    TYPE_OF_CAR_CHOICES = [
        (MOTOCYKL, "Motocykl"),
        (OSOBOWY, "Osobowy"),
        (CIEZAROWY, "Ciężarowy"),
    ]
    BENZYNA = "Benzyna"
    DIESEL = "Diesel"
    LPG = "LPG"
    TYPE_OF_CAR_FUEL_CHOICES = [
        (BENZYNA, "Benzyna"),
        (DIESEL, "Diesel"),
        (LPG, "LPG"),
    ]
    tytul = models.TextField()
    opis = models.TextField()
    kategoria = models.CharField(
        max_length=9,
        choices=TYPE_OF_CAR_CHOICES,
    )
    marka = models.TextField()
    model = models.TextField()
    rok_produkcji = models.IntegerField()
    przebieg = models.IntegerField()
    pojemnosc_skokowa = models.IntegerField()
    moc = models.IntegerField()
    rodzaj_paliwa = models.CharField(
        max_length=8,
        choices=TYPE_OF_CAR_FUEL_CHOICES
    )
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    zdjecie = models.ImageField(upload_to='car_pics')
    data_dodania = models.DateField()
    data_publikacji = models.DateField(default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.tytul} | {self.uzytkownik}"
