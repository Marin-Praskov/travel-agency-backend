from django.db import models

class Location(models.Model):
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    imageUrl = models.URLField()

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"


class Holiday(models.Model):
    title = models.CharField(max_length=200)
    startDate = models.DateField()
    duration = models.IntegerField()
    price = models.FloatField()
    freeSlots = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Reservation(models.Model):
    contactName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    holiday = models.ForeignKey(Holiday, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reservation by {self.contactName}"
