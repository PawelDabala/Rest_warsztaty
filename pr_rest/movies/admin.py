from django.contrib import admin
from movies.models import (
    Movie,
    Person,
    Movie_Characters
)


# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','year')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Movie_Characters)
class Movie_CharactersAdmin(admin.ModelAdmin):
    list_display = ('role',)

