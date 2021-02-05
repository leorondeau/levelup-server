from django.db import models

class Game(models.Model):

    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game_type = models.ForeignKey("GameTypes", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    number_of_players = models.IntegerField()
    description = models.CharField(max_length=250)

