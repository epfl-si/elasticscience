from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from publications.serializers import PublicationSerializer


@api_view(['POST'])
def populate(request):
    for record in request.data:
        serializer = PublicationSerializer(data=record)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
