from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=300)
    release_date = models.DateField()
    directors = models.CharField(max_length=300)
    actors = models.TextField()
    writers = models.CharField(max_length=300)
    genres = models.CharField(max_length=100)
    storyline = models.TextField(blank=True, null=True)
    trailer_url = models.URLField()
    cover = models.ImageField(upload_to="media")
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    