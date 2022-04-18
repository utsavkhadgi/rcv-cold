import json
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from api.movie.models import Movie, Genres
from api.movie.serializers import GenreSerializer, MovieSerializer

# Create your views here.


class MovieViewSet(ViewSet):
    #queryset = Movie.objects.all()
    # serializer_class = MovieSerializer

    def get_or_create_genre(self, genres):
        genre_ids = []
        for genre in genres:
            genre_ins, created = Genres.objects.get_or_create(
                name=genre.get('name'), defaults=genre)
            genre_ids.append(genre_ins.id)
        return genre_ids

    def update_or_create_genre(self, genres):
        genre_ids = []
        for genre in genres:
            genre_ins, created = Genres.objects.get_or_create(
                name=genre.get('name'),
                defaults=genre)
            genre_ids.append(genre_ins.id)
        return genre_ids

    def list(self, request):
        query = request.query_params.get("title")
        if query is not None:
            queryset = Movie.objects.filter(title__icontains=query)
            serializer = MovieSerializer(
                queryset, many=True, context={'request': request})
            return Response(serializer.data)
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True,
                                     context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            queryset = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({"error": "Movie Not found"}, status=404)
        serializer = MovieSerializer(
            queryset, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = MovieSerializer(
            data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        if not data.get('genres', None):
            return Response({"error": "Genre is required"})
        genres = json.loads(data['genres'])
        data.pop('genres', [])
        movie = serializer.save()
        genre_set = self.get_or_create_genre(genres)
        movie.genres.set(genre_set)
        return Response(serializer.data)

    def update(self, request, pk=None):
        movie = Movie.objects.get(pk=pk)
        data = request.data
        # movie.poster.delete(save=True)
        serializer = MovieSerializer(
            movie, request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        if not data.get('genres', None):
            return Response({"error": "Genre is required"})
        genres = json.loads(data['genres'])
        data.pop('genres', [])
        movie_ins = serializer.save()
        genre_set = self.update_or_create_genre(genres)
        movie_ins.genres.set(genre_set)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(
            {"detail": "Movie Deleted"},
            status=status.HTTP_200_OK)


class GenresViewSet(ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
