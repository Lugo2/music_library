from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MusicLibrarySerializer
from .models import Music

@api_view(['GET', 'POST'])
def music_list(request):
    
    if request.method == 'GET':
        music_type = request.query_params.get('type')
        queryset = Music.objects.all()
        if music_type:
            queryset = queryset.filter(music_type__type = music_type)

        serializer = MusicLibrarySerializer(queryset, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MusicLibrarySerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def music_library(request, pk):

    music_library = get_object_or_404(Music, pk = pk)

    if request.method == 'GET':
        serializer = MusicLibrarySerializer(music_library)
        return Response(serializer.id)

    elif request.method == 'PUT':
        serializer = MusicLibrarySerializer(music_library, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        music_library.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)