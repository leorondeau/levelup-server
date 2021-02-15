from django.db import models

class Event(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    scheduler = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    event_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=50)
    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
