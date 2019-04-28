from django.conf.urls import url, include

from rest_framework import routers

from .views import StarshipViewSet, ListingViewSet, create_listing


# Register viewsets
router = routers.DefaultRouter()
router.register(r'starships', StarshipViewSet)
router.register(r'listings', ListingViewSet)


urlpatterns = [
    url(r'', include(router.urls)),
    url(r'listing', create_listing),
    url(r'^api-auth/', include('rest_framework.urls')),
]
