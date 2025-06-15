from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class DrinkVariety(models.Model):
    DRINK_CHOICES = [('CF', 'COFFEE'),
                     ('TE', 'TEA'),
                     ('CP', 'CAPPUCCINO'),
                     ('LT', 'LATTE'),
                     ('EP', 'ESPRESSO'),
                     ('OJ', 'ORANGE JUICE'),
                     ('AJ', 'APPLE JUICE'),
                     ('CL', 'COLA'),
                     ('LM', 'LEMONADE'),
                     ('MS', 'MILKSHAKE'),
                     ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='imgs')
    data_add = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=DRINK_CHOICES, default='CF')
    description = models.TextField(max_length=1000, default='')
    price = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(10000)
    ])

    def __str__(self):
        return self.name
