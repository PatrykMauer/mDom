from django.db import models
from datetime import datetime
from realtors.models import Realtor



# Create your models here.

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    category = models.CharField(max_length=100, choices=[('Mieszkanie', 'Mieszkanie'), ('Dom', 'Dom'), ('Działka','Działka'),('Lokal','Lokal')])
    commission = models.BooleanField()
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    transaction = models.CharField(max_length=100, choices=[('Wynajem', 'Wynajem'), ('Sprzedaż', 'Sprzedaż')])
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    floor = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=2)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    list_data = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
