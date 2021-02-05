from django.db import models

class EventGamer(models.Model):

    event = models.ForeignKey("Events", on_delete=models.CASCADE)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)