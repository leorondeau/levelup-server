from django.db import models
from django.db.models.fields import CharField

class GameType(models.Model):

    label = CharField(max_length=50)