from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.movie.views import GenresViewSet

from api.movie.views import MovieViewSet
router = DefaultRouter()
router.register(r'movie', MovieViewSet, basename="movie")
router.register(r'genre', GenresViewSet, basename="genre")

urlpatterns = [
    path('', include(router.urls)),
]
