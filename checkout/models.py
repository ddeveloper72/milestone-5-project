from django.db import models
from issue_tracker.models import Issue
from django.contrib.auth.models import User

# Create your models here.


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    address_line_1 = models.CharField(max_length=40, blank=False)
    address_line_2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()
    buyer = models.ForeignKey(User, default=None,
                              related_name="feature_buyer",
                              on_delete=models.CASCADE)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
# Returning a string which is a summary of the order


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              null=False)
    product = models.ForeignKey(Issue,
                                on_delete=models.CASCADE,
                                null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.title,
                                      self.product.price)
# Return a string of the individual order line
# Create your models here.
