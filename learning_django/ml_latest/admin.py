from django.contrib import admin

from .models import Movies, Links, Ratings, Tags

# Register your models here.
admin.site.register(Movies)
admin.site.register(Links)
admin.site.register(Ratings)
admin.site.register(Tags)