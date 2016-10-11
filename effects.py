from inventory import Inventory
from copy import deepcopy

class Effect:
    def __init__(self):
        pass

    def event(self, game, player, event):
        pass

    def _expire(self, player):
        try:
            player.effects.remove(self)
        except ValueError:
            pass

class ExpiringEffect(Effect):
    time = 1

    def __init__(self):
        self.time = type(self).time

    def expire(self, game, player):
        pass

    def event(self, game, player, event):
        if event == "move":
            self.time -= 1
            if self.time == 0:
                self.expire(game, player)
                self._expire(player)

class Stun(Effect):
    def __init__(self, time):
        self.time = time

    def event(self, game, player, event):
        if event == "before_move":
            game.log("Вы пропускаете ход")
            self.time -= 1
            if self.time == 0:
                self._expire(player)
            game.next_move()
        else:
            super(Stun, self).event(game, player, event)

class Sleep(Effect):
    def __init__(self, time, start_position):
        self.time = time
        self.start_position = start_position

    def expire(self, game, player):
        game.players.remove(player.spirit)
        self._expire(player)
        player.active = True
        game.log("Вот что на самом деле лежит в вашей сумке: {}".format(player.inventory))

    def event(self, game, player, event):
        super(Sleep, self).event(game, player, event)
        if event == "start":
            player.spirit = deepcopy(player)
            player.sleep = self
            player.spirit.effects.pop() #remove this effect
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

    def expire(self, game, player):
        game.log(player, "Вы проснулись")
        player.body.sleep.expire(game, player.body)

    def event(self, game, player, event):
        super(Dream, self).event(game, player, event)
        if event == "start":
            player.body = self.body
        if event == "win":
            game.log("Какой приятный был сон!")
            self.expire(game, player)
            return True
        elif event == "die":
            game.log("Кошмар. Ну и приснится же такое!")
            self.expire(game, player)
            return True
