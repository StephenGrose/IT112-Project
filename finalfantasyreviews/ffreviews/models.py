from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class ffGame(models.Model):
    gameTitle=models.CharField(max_length=255)
    gameReleaseDate=models.DateField()
    gameReleasePlatform=models.TextField()
    gameSummary=models.TextField()

    def __str__(self):
        return self.gameTitle

    class Meta:
        db_table='games'

class ffReview(models.Model):
    reviewTitle=models.CharField(max_length=255)
    reviewDate=models.DateField()
    reviewBody=models.TextField()
    reviewRating=models.PositiveIntegerField(default=3,validators=[MinValueValidator(1),MaxValueValidator(5)])
    userID=models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.reviewTitle

    class Meta:
        db_table='reviews'