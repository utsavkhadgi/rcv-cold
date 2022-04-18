from asyncio.windows_events import NULL
from re import A
from rest_framework import serializers

from api.movie.models import Movie, Genres


class MovieListSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField(
        view_name="movie-detail")

    class Meta:
        model = Movie
        fields = ('id', 'title',)


class GenreSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField(
        view_name="genre-detail", read_only=True)

    movies = serializers.SerializerMethodField()

    class Meta:
        model = Genres
        fields = ('id', 'name', 'created_at', 'updated_at', "movies")
        read_only_fields = ('id', 'created_at',
                            'updated_at', 'movies')

    def get_movies(self, obj):
        movies = MovieListSerializer(
            data=obj.movies.all(),
            many=True, context={'request': self.context['request']})
        movies.is_valid()
        return movies.data


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        read_only=True, many=True, slug_field='name')
    poster = serializers.ImageField(
        allow_empty_file=True, required=False)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'language',
                  'overview', 'poster', 'year', 'genres',)
        read_only_fields = ('id', 'created_at', 'updated_at',)
        depth = 1
    # def get_genres(self, obj):
    #     genres = obj.genres.all()
    #     genre_serializer = GenreSerializer(genres, many=True)
    #     return genre_serializer.data

    # def get_or_create_genres(self, genres):
    #     genres_id = []
    #     for genre in genres:
    #         genre_instance, created = Genres.objects.get_or_create(
    #             pk=genre.get('id'), defaults=genre)
    #         genres_id.append(genre_instance.pk)
    #     return genres_id

    # def update_or_create_genres(self, genres):
    #     genres_id = []
    #     for genre in genres:
    #         genre_instance, created = Genres.objects.update_or_create(
    #             pk=genre.get('id'), defaults=genre)
    #         genres_id.append(genre_instance.pk)
    #     return genres_id

    # def create(self, validated_data):
    #     genres = validated_data.pop('genres', [])
    #     movie = self.Meta.model.objects.create(**validated_data)
    #     movie.genres.set(self.get_or_create_genres(genres))
    #     return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.language = validated_data.get(
            'language', instance.language)
        instance.overview = validated_data.get(
            'overview', instance.overview)
        if validated_data.get('poster'):
            instance.poster.delete(save=True)
            instance.poster = validated_data.get(
                'poster', instance.poster)
        else:
            instance.poster = validated_data.get(
                'poster', instance.poster)
        instance.year = validated_data.get('year', instance.year)
        instance.save()
        return instance
