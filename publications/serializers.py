from rest_framework import serializers

from .models import Publication


class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publication
        fields = ('title', 'pub_date')
