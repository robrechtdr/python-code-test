from django.db import models

from .errors import UnrecognisedValueError, EntryAlreadyExistsError


class Starship(models.Model):
    starship_class = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    # null=True as we want to capture 'unknown' vals.
    length = models.FloatField(null=True)
    hyperdrive_rating = models.FloatField(null=True)
    cargo_capacity = models.BigIntegerField(null=True)
    crew = models.IntegerField(null=True)
    passengers = models.IntegerField(null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ListingManager(models.Manager):
    def create_listing(self, listing_name, starship_type, 
        price, get_or_create=False):

        starship_type_ = Starship.objects.filter(
            name__iexact=starship_type).first()

        if not starship_type_:
            raise UnrecognisedValueError(f"Starship type '{starship_type}' "
                "is not a recognized type. Please use a recognized "
                "starship type (e.g. 'AA-9 Coruscant freighter').")

        if get_or_create:
            return Listing.objects.get_or_create(name=listing_name, 
                ship_type=starship_type_, price=price)
        else:
            return Listing.objects.create(name=listing_name, 
                ship_type=starship_type_, price=price)


class Listing(models.Model):
    name = models.CharField(max_length=255)
    # https://www.valentinog.com/blog/django-missing-argument-on-delete/
    ship_type = models.ForeignKey(Starship, related_name='listings', 
        on_delete=models.PROTECT)
    price = models.BigIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ListingManager()

    def __str__(self):
        return self.name
