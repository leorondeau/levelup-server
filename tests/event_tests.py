import json
from unittest.loader import defaultTestLoader
from rest_framework import status
from rest_framework.test import APITestCase
from levelupapi.models import GameType
from levelupapi.models import Game
from levelupapi.models import Event
from levelupapi.models import Gamer


class EventTests(APITestCase):
    def setUp(self):

        url = "/register"
        data = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "first_name": "Steve",
            "last_name": "Brownlee",
            "bio": "Love those gamez!!"
        }

        response = self.client.post(url, data, format='json')

        json_response = json.loads(response.content)

        self.token = json_response["token"]

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        gametype = GameType()
        gametype.label = "Board game"
        
        gametype.save()
        game = Game()
        game.game_type = gametype
        game.title = "Balderdash"
        game.number_of_players = 4
        game.gamer_id = 1
        game.save()
       
        
    def test_create_event(self):

        url ="/events"
        data = {
            "gameId": 1,
            "scheduler": 1,
            "eventTime": "2021-02-27 08:30:00",
            "location": "home",
            "gameTypeId": 1
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        response = self.client.post(url, data, format='json')

        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json_response["event_time"], "2021-02-27 08:30:00")
        self.assertEqual(json_response["location"], "home")
