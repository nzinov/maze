class Event:
    name = None


class AfterChose(Event):
    name = 'after_choice'

    def __init__(self, action):
        self.action = action


class AfterMove(Event):
    name = 'after_move'

    def __init__(self, direction):
        self.direction = direction
