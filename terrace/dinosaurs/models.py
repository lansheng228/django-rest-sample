from django.db import models


class Dinosaur(models.Model):
    species = models.TextField()
    class Meta:
        db_table = 'dinosaur'

