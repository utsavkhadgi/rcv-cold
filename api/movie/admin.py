from django.contrib import admin

from .models import Genres, Movie

# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'overview',
                    'language', 'poster', 'year', ]


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', ]


admin.site.register(Genres, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
