from django.db import models
from datetime import datetime
from product.models import Product
from accounts.models import Account
from customer.models import AddressDetails

# Create your models here.
class Transaction(models.Model):
    date = models.DateTimeField(auto_now_add=datetime.now())
    amount = models.FloatField(null=False, blank=False, unique=False)
    customer = models.ForeignKey(Account, models.CASCADE)
    shipping = models.ForeignKey(AddressDetails, models.CASCADE)


class TransactionItem(models.Model):
    choices = [(2, "Dispatched"), (3, "Delivered"), (1, "Pending")]
    product = models.ForeignKey(Product, models.CASCADE)
    transaction = models.ForeignKey(Transaction, models.CASCADE)
    status = models.IntegerField(choices=choices, default=1)
    quantity = models.PositiveIntegerField()

    @property
    def get_transaction_date(self):
        return self.transaction.date

    @property
    def get_shipping(self):
        return self.transaction.shipping