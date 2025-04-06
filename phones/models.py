from django.db import models


class Phone(models.Model):
    id_phone = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    image = models.URLField(default='https://t4.ftcdn.net/jpg/07/60/69/29/360_F_760692902_CSWwEZ356IjrXP4nRluyRpsG0Xpr7VRl.jpg')
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()

