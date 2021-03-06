from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Gin(models.Model):
    name = models.CharField(max_length=200, unique=True)
    bio = models.TextField(max_length=500)
    size = models.PositiveIntegerField()
    abv = models.FloatField()
    image = models.CharField(max_length=500, unique=True)
    price = models.FloatField()
    origin = models.CharField(max_length=200)
    botanicals = models.CharField(max_length=200)
    tasting_notes = models.TextField(max_length=500)
    perfect_gt = models.CharField(max_length=200)
    flavour = models.CharField(max_length=50)
    is_premium = models.BooleanField()
    liked_by = models.ManyToManyField(
        'jwt_auth.User',
        related_name='liked_gins',
        blank=True
    )

    def __str__(self):
        return f'{self.name}'

class Comment(models.Model):
    text = models.TextField(max_length=300)
    rated = models.PositiveIntegerField(default=10, validators=[MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    gin = models.ForeignKey(
        Gin,
        related_name='comments',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='comments_made',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.gin} - {self.id}'
