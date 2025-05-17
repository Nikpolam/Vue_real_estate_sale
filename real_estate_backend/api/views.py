from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Property, PropertyImage, Favorite
from .serializers import PropertySerializer, PropertyImageSerializer, FavoriteSerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['post'])
    def favorite(self, request, pk=None):
        property = self.get_object()
        favorite, created = Favorite.objects.get_or_create(
            user=request.user,
            property=property
        )
        if not created:
            favorite.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(FavoriteSerializer(favorite).data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def my_properties(self, request):
        properties = Property.objects.filter(owner=request.user)
        serializer = self.get_serializer(properties, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def my_favorites(self, request):
        favorites = Favorite.objects.filter(user=request.user)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data)

class PropertyImageViewSet(viewsets.ModelViewSet):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        property_id = self.request.data.get('property')
        property = get_object_or_404(Property, id=property_id)
        if property.owner != self.request.user:
            return Response(
                {"detail": "You can only add images to your own properties."},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer.save() 