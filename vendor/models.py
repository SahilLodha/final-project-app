from django.db import models
from accounts.models import Account
from django.core.validators import FileExtensionValidator


class VendorDescription(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    vendor_logo = models.ImageField(validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    vendor_background = models.ImageField(validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])