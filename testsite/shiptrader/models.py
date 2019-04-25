from django.db import models


class Starship(models.Model):
    starship_class = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)

    length = models.FloatField()
    hyperdrive_rating = models.FloatField()
    cargo_capacity = models.BigIntegerField()

    crew = models.IntegerField()
    passengers = models.IntegerField()


class Listing(models.Model):
    name = models.CharField(max_length=255)
    # https://www.valentinog.com/blog/django-missing-argument-on-delete/
    ship_type = models.ForeignKey(Starship, related_name='listings', on_delete=models.PROTECT)
    price = models.IntegerField()
