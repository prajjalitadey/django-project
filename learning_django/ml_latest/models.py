from __future__ import unicode_literals

from django.db import models

class Movies(models.Model):
    movieid = models.IntegerField()
    title = models.CharField(max_length = 150)
    genres = models.CharField(max_length = 200)



class Links(models.Model):
    movieid = models.IntegerField()
    imdb_id = models.IntegerField()
    tmdb_id = models.IntegerField(null = True)
    
    
    
    
class Ratings(models.Model):
    userid = models.IntegerField()
    movieid = models.IntegerField()
    rating = models.FloatField()
    timestamp = models.DateTimeField()
    
    
    
    
class Tags(models.Model):
    userid = models.IntegerField()
    movieid = models.IntegerField()
    tag = models.CharField(max_length = 300)
    timestamp = models.DateTimeField()
#    
