FIELD = """2
8
a: : |B| : : :d
=+=+.+ +.+.+.+.
E: | : :D: | :V
=+.+.+.+ +.+.+.
A: |>: :<| : :C
.+.+.+=+=+=+=+.
 |R|3: :Z:R: : 
.+.+.+=+.+.+.+.
V: :2|T| : | : 
.+.+.+=+.+=+.+.
 : |1: : |B: : 
.+.+=+=+.+.+=+ 
B| : :C| : | :A
=+.+.+.+.+=+ +=
b: :<: :   : :c
4
 : :>:<
.+.+.+.
 : : : 
.+=+.+.
 :B:T: 
=+.+.+.
E: | :^
B Stuff({"бутылка": 1})
E Exit(LEFT)
T Stuff({"сокровище": 1})
A Armory()
C Stuff({"дубина": 1})
R Stuff({"скакалка": 1})
Z EffectorSquare(lambda: Sleep(7, Position(1, 3, 2)))
D EffectorSquare(lambda: Sleep(4, Position(1, 0, 3)))
a Hole(Position(0, 7, 7))
b Hole(Position(0, 0, 7))
c Hole(Position(0, 0, 0))
d Hole(Position(0, 7, 0))
1 River(Position(0, 4, 2))
2 River(Position(0, 3, 2))
3 River(Position(0, 2, 2))
V RubberRoom(DOWN)
^ RubberRoom(UP)
> RubberRoom(RIGHT)
< RubberRoom(LEFT)
"""
from objects import Object, register_object
from effects import Effect
from player import Player
from constants import DIRECTIONS


class FeelMyPower(Effect):

    def event(self, game, player, event):
        super(FeelMyPower, self).event(game, player, event)
        if isinstance(player, Geanie):
            return False
        if event == "before_move":
            for other in game.players:
                if (other.position == player.position
                        and isinstance(other, Geanie)
                        and player is not other.master):
                    game.log("Вы не можете пошевелиться, настолько страшен вид этого джина")
                    game.next_move()
        return False

class Geanie(Player):

    def __init__(self, master):
        super(Geanie, self).__init__("Джин ибн {}".format(master.name), master.position)
        self.master = master
        self.pid = master.pid
        self.inventory.add("ятаган")
        self.live = 5

    def disappear(self, game):
        game.log(self, "Я ХОРОШО ПОСЛУЖИЛ ТЕБЕ, ПОВЕЛИТЕЛЬ. прощай...")
        self._die(game)
        game.players.remove(self)


    def event(self, game, event):
        if event == "before_move":
            game.log("СЛУШАЮ И ПОВИНУЮСЬ")
        prevent_default = super(Geanie, self).event(game, event)
        if not prevent_default:
            if event == "die":
                self.disappear(game)
                return True
            elif event == "win":
                game.log("ТЫ ШУТИШЬ, ПОВЕЛИТЕЛЬ! КАК Я МОГУ ПРОЛЕЗТЬ В ЭТО ИГОЛЬНОЕ УШКО?!")
                return True


@register_object("ятаган")
class Yataghan(Object):
    """в/н/л/п - сломать стену в заданном направлении"""

    @staticmethod
    def action(game, player, action):
        if not isinstance(player, Geanie):
            game.log("Его и нести-то тяжело, куда уж тут махать")
            return None
        if action in DIRECTIONS:
            direction = DIRECTIONS[action]
            if not game.field.is_legal(player.position + direction):
                game.log("Джин наносит сокрушительные удары, но все тщетно - стена стоит нерушимо")
            elif game.field.can_move(player.position, direction):
                game.log("Ятаган рассек воздух")
            else:
                game.log("Пара мощных ударов - и стены как не бывало")
                game.log("РАД СТАРАТЬСЯ, ПОВЕЛИТЕЛЬ")
                subfield = game.field.fields[player.position.field]
                position = player.position
                if direction[0] == 0:
                    subfield.vert_walls[position.x()][position.y() + min(0, direction[1])] = False
                else:
                    subfield.hor_walls[position.x() + min(0, direction[0])][position.y()] = False
            return False


@register_object("бутылка")
class Bottle(Object):
    """Старая замшелая бутылка с большой сургучной печатью на пробке. Может открыть?"""

    @staticmethod
    def action(game, player, action):
        if action == "открыть":
            game.log("Раздался страшный треск, из бытылки пошел дым и появился джин.")
            game.log("БЛАГОДАРЮ ТЕБЯ, ОСВОБОДИВШЕГО МЕНЯ ИЗ ЗАТОЧЕНИЯ")
            game.log("Я ПОЙДУ, КУДА ТЫ ПРИКАЖЕШЬ И СОКРУШУ ЛЮБЫЕ СТЕНЫ СВОИМ ЯТАГАНОМ")
            game.log("ТВОИ ВРАГИ ОНЕМЕЮТ ОТ СТРАХА ЕДВА ЗАВИДЯ МЕНЯ")
            for other in game.players:
                if not isinstance(other, Geanie):
                    other.add_effect(game, FeelMyPower())
            game.players.append(Geanie(player))
            return True

@register_object("зачарованная_бутылка")
class CharmedBottle(Object):
    """Эта бутылка так и тянет к себе. Наверное, чуть только зазеваешься, сразу же затянет. Жутковато.
    Наверное, если наклонить ее вбок (в/н/л/п), то затянет даже из соседней комнаты
    """

    @staticmethod
    def action(game, player, action):
        if action in DIRECTIONS:
            direction = DIRECTIONS[action]
            if not game.field.can_move(player.position, direction):
                game.log("Какой толк поворачивать туда бутылку? Там же стена")
            else:
                for other in game.players:
                    if other.position == player.position + direction and isinstance(other, Geanie):
                        other.disappear(game)
                        game.log("Раздался легкий свист и... скорее, где пробка?!")
                        player.inventory.add("бутылка")
                        return True
            game.log("Кажется, затея не удалась")
            return False
