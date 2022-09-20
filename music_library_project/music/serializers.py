from rest_framework import serializers
from .models import MusicLibrary

class MusicLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicLibrary
        fields = ['id', 'tile','artist','album','release_date','genre']
        depth = 1