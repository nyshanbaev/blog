from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from applications.feedback.models import Favorite
from applications.feedback.serializers import FavoriteSerializers
from rest_framework.permissions import IsAuthenticated
class FavoriteModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)

        return queryset


