from django.db import models

# Create your models here.
# Pension model

class Pension(models.Model):
    fullname = models.CharField(max_length=100, blank=False, null=False),
    email = models.EmailField(unique=True, blank=False, null=False),
    phone = models.CharField(max_length=11, blank=False, null=False),
    rsa = models.CharField(max_length=100, blank=False, null=False),
    pfa = models.CharField(max_length=100, blank=False, null=False),
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False),
    isActive = models.BooleanField(default=True, blank=False, null=False),


    def __str__(self):
        return self.fullname



class Pen(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    rsa = models.CharField(max_length=20)
    pfa = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    isActive = models.BooleanField(default=False)

    def __str__(self):
        return self.fullname



