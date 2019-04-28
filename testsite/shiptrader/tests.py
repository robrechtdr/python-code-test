from django.test import TestCase
from django.urls import reverse
from django.core.management import call_command

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Listing


class ApiTests(APITestCase):
    # We only want to run this once for test suite.
    # 
    # Also, no need for a teardown as for each new test run the 
    # db is flushed: https://stackoverflow.com/questions/9459030/django-when-to-use-teardown-method.
    @classmethod
    def setUpClass(cls):
        # https://stackoverflow.com/questions/29653129/update-to-django-1-8-attributeerror-django-test-testcase-has-no-attribute-cl
        super(ApiTests, cls).setUpClass()
        call_command("dummy_populate")


    def test_browse_starships(self):
        response = self.client.get("/starships/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 37)

        first_starship = response.json()[0]
        self.assertEqual(first_starship["name"], "Executor")
        self.assertEqual(first_starship["crew"], 279144)


    def test_get_specific_starship_class_listings(self):
        response = self.client.get("/listings/")
        self.assertEqual(len(response.json()), 4)

        starship_class = "starfighter"
        sf_response = self.client.get(f"/listings/?search={starship_class}")

        self.assertEqual(len(sf_response.json()), 2)


    def test_get_price_sorted_listings(self):
        response = self.client.get("/listings/")
        self.assertEqual(response.json()[0]["price"], 50000)


        response = self.client.get("/listings/?ordering=-price")
        self.assertEqual(response.json()[0]["price"], 80000000)


    def test_get_time_sorted_listings(self):
        response = self.client.get("/listings/")
        self.assertEqual(response.json()[0]["name"], "Beautiful Jedi Starfighter")

        jedi_starfighter = Listing.objects.create_listing(
            listing_name="Barely damaged Millennium Falcon",
            starship_type="Millennium Falcon",
            price=890000) 

        response = self.client.get("/listings/?ordering=-created_at")
        self.assertEqual(response.json()[0]["name"], "Barely damaged Millennium Falcon")

        # Clean up
        Listing.objects.get(pk=jedi_starfighter.id).delete()


    def test_list_starship_for_sale(self):
        data = {
            "listing_name": "Barely damaged Millennium Falcon",
            "starship_type": "Millennium Falcon",
            "price": 890000
        } 

        response = self.client.post("/listing/", data=data)

        mill_falcon_listing = Listing.objects.get(name=data["listing_name"])
        self.assertEqual(mill_falcon_listing.name, data["listing_name"])

        # Clean up
        Listing.objects.get(pk=mill_falcon_listing.id).delete()


    def test_deactivate_listing(self):
        self.client.patch("/listings/1/", data={"is_active": False})

        response = self.client.get("/listings/1/")
        self.assertEqual(response.json()["is_active"], False)

        # Clean up
        self.client.patch("/listings/1/", data={"is_active": True})
