from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Tutorial
from .serializers import TutorialSerializer


class TutorialsViewSet(ModelViewSet):
    serializer_class = TutorialSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        If the title query param is provided, then get it and filter the 
        tutorials.
        """
        title_start = self.request.query_params.get('title', None)
        if title_start is not None:
            queryset = Tutorial.objects.all().filter(
                title__icontains=title_start)
        else:
            queryset = Tutorial.objects.all()

        return queryset

    @action(methods=['GET'],
            detail=False,
            permission_classes=[IsAuthenticatedOrReadOnly],
            url_path='published')
    def get_published_tutorials(self, request):
        """Return only published tutorials"""
        queryset = Tutorial.objects.filter(published=True).all()
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
