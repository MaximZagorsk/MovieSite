from django.contrib import admin
from .models import Category, Genre, Movie, Actor, Rating, \
    Reviews, RatingStar, MovieShots

# Register your models here.
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Reviews)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Actor)
