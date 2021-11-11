from django.db import models
from orders.models import OrderItem
# Create your models here.

class InventoryAccount(models.Model):

    name = models.CharField(max_length=150)

    def sum(self):
        sum_x=0
        all_transactions = self.transactions.all()
        for transaction in all_transactions:
            sum_x+= transaction.quantity
        return sum_x

    def __str__(self):
        return self.name


class InventoryTransaction(models.Model):
    account=models.ForeignKey(InventoryAccount, on_delete=models.CASCADE, related_name="transactions")
    created_on = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField()


