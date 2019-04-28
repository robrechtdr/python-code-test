from django.core.management.base import BaseCommand
from django.core.management import call_command

from shiptrader.models import Starship, Listing


class Command(BaseCommand):
    def handle(self, **options):
        """
        Populate dummy db entries for convenience.
        """
        call_command("import_starships")

        starships = Starship.objects.all()

        # Class: Starfighter
        jedi_starfighter = Listing.objects.create_listing(
            listing_name="Beautiful Jedi Starfighter",
            starship_type="Jedi starfighter",
            price=50000,
            get_or_create=True) 

        # Class: Starfighter
        x_wing = Listing.objects.create_listing(
            listing_name="Dented X-wing",
            starship_type="X-wing",
            price=7800808,
            get_or_create=True)

        # Class: Star Destroyer
        star_destroyer = Listing.objects.create_listing(
            listing_name="Breathtaking Star Destroyer",
            starship_type="Star Destroyer",
            price=780900,
            get_or_create=True) 

        # Class: Deep Space Mobile Battlestation
        death_star = Listing.objects.create_listing( 
            listing_name="Good as new Death Star",
            starship_type="Death Star",
            price=80000000,
            get_or_create=True) 

        print("Dummy population finished.")
