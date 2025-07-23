import random

from .effect import Effect, ExpiringEffect
from copy import deepcopy
from inventory import Inventory


def drop_sleep_loot(game, spirit):
    sleep_loot = spirit.body.inventory.get_excess(spirit.inventory)
    if game.debug:
        print('body loot', spirit.body.inventory, 'spirit loot', spirit.inventory, 'sleep loot', sleep_loot)
    game.field[spirit.position].loot.update(sleep_loot)


class Sleep(Effect):

    def __init__(self, time, start_position):
        self.time = time
        self.start_position = start_position

    def expire(self, game, player):
        drop_sleep_loot(game, player.spirit)
        game.replace_player(player.spirit, player)
        game.remove_player(player.spirit)
        self._expire(player)
        player.active = True

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
            game.replace_player(player, player.spirit)
            player.active = False
        elif event == "die":
            self.expire(game, player)
            return False

    def __str__(self):
        return 'Sleep({})'.format(self.time)


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
        elif event == "exit":
            drop_sleep_loot(game, player)
            player.inventory = Inventory()
        elif event == "win":
            game.log("Какой приятный был сон!")
            self.wake()
            return True
        elif event == "die":
            game.log("Кошмар. Ну и приснится же такое!")
            self.wake()
            return True

    def __str__(self):
        return 'Dream({})'.format(self.time)
