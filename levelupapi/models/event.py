from django.db import models

class Event(models.Model):

    game = models.ForeignKey("Games", on_delete=models.CASCADE)
    scheduler = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    event_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=50)

