from inventory import Inventory


class Player:

    def __init__(self, name, position):
        self.start_position = position
        self.position = position
        self.effects = []
        self.inventory = Inventory()
        self.name = name
        self.active = True
        self.pid = None

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

    def _die(self, game):
        game.log(self, "Вы умерли")
        game.field[self.position].loot.update(self.inventory)
        self.inventory = Inventory()
        self.position = self.start_position
        self.effects = []

    def die(self, game):
        if self.event(game, "die"):
            return
        self._die(game)

    def add_effect(self, game, effect):
        self.effects.append(effect)
        self.effects[-1].event(game, self, "start")

    def __str__(self):
        return self.name
