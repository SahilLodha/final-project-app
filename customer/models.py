from django.db import models
from accounts.models import Account


# Create your models here.
class AddressDetails(models.Model):
    customer = models.ForeignKey(Account, models.CASCADE)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    house_number = models.CharField(max_length=50)
    nearest_landmark = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'location'
        verbose_name_plural = 'locations'
        unique_together = ['customer', 'city', 'house_number']

    def __str__(self):
        return f'{self.country} | {self.city} | {self.house_number}'
