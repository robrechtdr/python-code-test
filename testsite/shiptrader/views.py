from django.core import serializers

from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Starship, Listing
from .serializers import StarshipSerializer, ListingSerializer


class StarshipViewSet(viewsets.ModelViewSet):
    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    # https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('=ship_type__starship_class',)


@api_view(["POST"])
def create_listing(request):
    listing = Listing.objects.create_listing(
        listing_name=request.data["listing_name"],
        starship_type=request.data["starship_type"],
        price=request.data["price"]) 

    ser_listing = serializers.serialize("json", [listing, ]) 
    return Response(ser_listing)
