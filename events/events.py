class Event:
    name = None


class AfterChoice(Event):
    """Event fired after player makes an action choice"""
    name = 'after_choice'

    def __init__(self, action):
        self.action = action


class AfterItemChoice(Event):
    """Event fired after player choses an action with item"""
    name = 'after_choice'

    def __init__(self, action):
        self.action = action


class AfterMove(Event):
    """Event fired after player moves"""
    name = 'after_move'

    def __init__(self, direction):
        self.direction = direction


class PlayerArrive(Event):
    """Event fired when player arrives to a new square"""
    name = 'player_arrive'


class PlayerExit(Event):
    """Event fired when player exits the game"""
    name = 'player_exit'


class PlayerDie(Event):
    """Event fired when player is to die"""
    name = 'player_die'


class EffectStart(Event):
    """Event fired on newly created effect"""
    name = 'effect_start'


class PlayerEndTurn(Event):
    """Event fired at end of player turn, after all actions"""
    name = 'player_end_turn'


class GameStartRound(Event):
    """Event fired for all players when the first player starts move"""
    name = 'game_start_round'


class PlayerStartTurn(Event):
    """Event fired at start of player turn, before any action"""
    name = 'player_start_turn'


class PlayerMove(Event):
    """Event fired after player move"""
    name = 'player_move'


class PlayerWin(Event):
    """Event fired when player is to win"""
    name = 'player_win'
