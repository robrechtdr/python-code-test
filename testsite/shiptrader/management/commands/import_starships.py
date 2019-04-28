from django.core.management.base import BaseCommand

from shiptrader.models import Starship
# no 'import swapi' as lib is python 2.7.x
import requests


class Command(BaseCommand):
    def handle(self, **options):
        """
        Import starships from swapi (star wars api).

        This process is idempotent; it will not create duplicate
        entries on repeated runs.
        """
        print("Importing starships ...")
        def create_starship_entries(starships):
            for starship in starships:
                cargo_capacity = starship["cargo_capacity"]
                if cargo_capacity.lower() == "unknown":
                    cargo_capacity = None

                passengers = starship["passengers"]
                if passengers.lower() == "unknown":
                    passengers = None

                crew = starship["crew"]
                if crew.lower() == "unknown":
                    crew = None

                length = starship["length"].replace(",", "")
                if length.lower() == "unknown":
                    length = None

                hyperdrive_rating = starship["hyperdrive_rating"]
                if hyperdrive_rating.lower() == "unknown":
                    hyperdrive_rating = None

                starship = Starship.objects.get_or_create(
                    name=starship["name"], 
                    starship_class=starship["starship_class"], 
                    manufacturer=starship["manufacturer"], 
                    length=length, 
                    hyperdrive_rating=hyperdrive_rating,
                    cargo_capacity=cargo_capacity,
                    crew=crew, 
                    passengers=passengers)

        url = "https://swapi.co/api/starships"
        while url:
            req = requests.get(url).json()
            print(f"\tImporting starships from {url} ...")
            create_starship_entries(req["results"])
            print("\tDone")
            url = req["next"]

        print(f"Finished importing starships.")
