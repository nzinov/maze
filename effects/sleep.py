import random

from .effect import Effect, ExpiringEffect
from copy import deepcopy
from inventory import Inventory


class Sleep(Effect):

    def __init__(self, time, start_position):
        self.time = time
        self.start_position = start_position

    def expire(self, game, player):
        game.players.remove(player.spirit)
        self._expire(player)
        player.active = True
        health_addition = random.choice([-5, 0, 5, 10, 15, 20])
        player.health += health_addition

        game.log("Вот что на самом деле лежит в вашей сумке: {}".format(
            player.inventory))

    def event(self, game, player, event):
        super(Sleep, self).event(game, player, event)
        if event == "start":
            player.spirit = deepcopy(player)
            player.sleep = self
            player.spirit.effects.pop()  # remove this effect
            player.spirit.position = self.start_position
            player.spirit.add_effect(game, Dream(self.time, player))
            game.players.insert(game.current_player, player.spirit)
            player.active = False
        elif event == "die":
            self.expire(game, player)
            return False


class Dream(ExpiringEffect):

    def __init__(self, time, body):
        self.time = time
        self.body = body

    def wake(self):
        self.time = 0

    def expire(self, game, player):
        game.log(player, "Вы проснулись")
        player.body.sleep.expire(game, player.body)

    def event(self, game, player, event):
        super(Dream, self).event(game, player, event)
        if event == "start":
            player.body = self.body
        if event == "win":
            game.log("Какой приятный был сон!")
            self.wake()
            return True
        elif event == "die":
            game.log("Кошмар. Ну и приснится же такое!")
            self.wake()
            return True
