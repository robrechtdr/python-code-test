from rest_framework import serializers
from .models import Starship, Listing


class StarshipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Starship
        fields = '__all__'


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
