from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PublicationSerializer
from .search import search


@api_view(['POST'])
def populate(request):
    serializer = PublicationSerializer(many=True, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def search_exact(request, author):
    hits = search(author).hits.hits
    publications = [hit.get('_source') for hit in hits]

    serializer = PublicationSerializer(many=True, data=publications)

    if serializer.is_valid():
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
