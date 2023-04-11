from django.db import models


class SheetData(models.Model):
    number = models.IntegerField(primary_key=True)
    order_number = models.IntegerField()
    cost_usd = models.FloatField()
    delivery_date = models.DateField()
    cost_rub = models.DecimalField(max_digits=100, decimal_places=4)
