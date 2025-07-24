from inventory import Inventory


class Player:
    MAX_HEALTH = 100

    def __init__(self, name, position, pid):
        self.start_position = position
        self.position = position
        self.effects = []
        self.inventory = Inventory()
        self.name = name
        self.active = True
        self.pid = pid
        self._health = self.MAX_HEALTH

    def get_state(self):
        return self.name, self.pid, self.position, self.effects, self.inventory, self.active, self._health

    def event(self, game, event):
        """
        Fire corresponding effect for all effects on this player and square

        List of events:
        name - when fired - default action
        ---------------------------------
        move - after player move
        before_move - before player move - proceed to the move
        start - fired on newly created effect
        die - player is to die - kill player
        win - player is to win - finish game
        exit - player exits the game
        arrive - player arrives to a new square
        start_turn - fired for all players when the first player starts move

        """
        prevent_default = False
        for effect in self.effects:
            if effect.event(game, self, event):
                prevent_default = True
        if game.field[self.position].event(game, self, event):
            prevent_default = True
        return prevent_default

    def drop_loot(self, game):
        game.field[self.position].loot.update(self.inventory)
        self.inventory = Inventory()

    def exit(self, game, recurse=True):
        self.event(game, "exit")
        self.drop_loot(game)
        if self.active:
            game.log('Игрок {} покинул игру'.format(self))

        game.remove_player(self)
        if recurse:
            for player in game.players:
                if player.pid == self.pid:
                    player.exit(game, False)
        return True

    def _die(self, game):
        game.log(self, "Вы умерли")
        self.drop_loot(game)
        self.position = self.start_position
        self.effects = []
        self._health = self.MAX_HEALTH

    def die(self, game):
        if self.event(game, "die"):
            return False
        self._die(game)
        return True

    def add_effect(self, game, effect):
        self.effects.append(effect)
        self.effects[-1].event(game, self, "start")

    def __str__(self):
        return "@" + self.name

    def name_as_hashtag(self):
        return "#" + self.name

    @property
    def health(self):
        return self._health

    def change_health(self, game, health_delta):
        old_health = self._health
        self._health = min(self.MAX_HEALTH, self._health + health_delta)
        if old_health != self._health:
            if health_delta > 0:
                health_delta_str = ":green_heart: +" + str(health_delta)
            else:
                health_delta_str = ":heart: " + str(health_delta)
            game.log(str(self) + ": " + health_delta_str)
        if self._health <= 0:
            self.die(game)
