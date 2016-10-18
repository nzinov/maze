from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import TOKEN
from game import Game, GameEnded
from reader import read_field
from player import Player
from random import shuffle
import dill as pickle
from emoji import emojize


class TelegramController:
    instances = {}

    @classmethod
    def wait(cls):
        cls.updater = Updater(token=TOKEN)
        cls.updater.dispatcher.add_handler(CommandHandler('start', cls.create))
        cls.updater.dispatcher.add_handler(CommandHandler('go', cls.go))
        cls.updater.dispatcher.add_handler(CommandHandler('ready', cls.ready))
        cls.updater.dispatcher.add_handler(
            MessageHandler([Filters.text], cls.on_message))
        try:
            with open("pickle.bin", "rb") as f:
                cls.instances = pickle.load(f)
        except FileNotFoundError:
            pass
        cls.updater.start_polling()
        cls.updater.idle()

    @staticmethod
    def create(bot, update):
        instance = TelegramController(
            bot, update.message.chat_id, update.message.text.split()[1])
        TelegramController.instances[update.message.chat_id] = instance
        instance.start()

    @staticmethod
    def go(bot, update):
        _, chat_id, name, pos = update.message.text.split()
        pid = update.message.from_user.id
        chat_id = int(chat_id)
        if not chat_id in TelegramController.instances:
            update.message.reply_text("Недопустимый номер игры")
            return
        TelegramController.instances[chat_id].add(update, pid, name, pos)

    def __init__(self, bot, chat_id, fname):
        self.bot = bot
        self.field = read_field(fname)
        self.chat_id = chat_id
        self.players = []
        self.accept_players = True
        self.game = None

    def start(self):
        self.log("Начинается игра!")
        self.log("Поле имеет размеры {0}x{0}".format(
            self.field.fields[0].size))
        self.log(
            'Чтобы присоединиться, напишите мне в личку "/go {} <имя> <начальная позиция>"'.format(self.chat_id))
        self.log(
            "Маленькие английские буквы по горизонтали, цифры с нуля по вертикали")
        self.log(self.field.description)

    def add(self, update, pid, name, pos):
        if not self.accept_players:
            update.message.reply_text("К этой игре нельзя присоединиться")
        try:
            x = int(pos[1])
            y = ord(pos[0]) - ord('a')
            pos = Position(0, x, y)
            if not self.field.is_legal(pos):
                raise ValueError
        except ValueError:
            update.message.reply_text("Недопустимая позиция")
        else:
            self.players.append(Player(name, pos))
            self.players[-1].pid = pid
            update.message.reply_text("Отлично")
            self.log("Присоединился игрок {}".format(name))

    @staticmethod
    def ready(bot, update):
        if update.message.chat_id in TelegramController.instances:
            self = TelegramController.instances[update.message.chat_id]
            self.accept_players = False
            self.log("Игра началась")
            self.log("Пишите 'помощь' в свой ход, чтобы узнать, что делать")
            shuffle(self.players)
            self.game = Game(self, self.field, self.players)

    def log(self, message):
        self.bot.sendMessage(chat_id=self.chat_id,
                             text=emojize(message, use_aliases=True))

    def action(self, message):
        action = message.text
        if not self.game:
            return
        if message.from_user.id != self.game.players[self.game.current_player].pid:
            return
        try:
            self.game.action(action)
        except GameEnded:
            pass

    @staticmethod
    def on_message(bot, update):
        with open("pickle.bin", "wb") as f:
            pickle.dump(TelegramController.instances, f)
        if update.message.chat_id in TelegramController.instances:
            TelegramController.instances[update.message.chat_id].bot = bot
            TelegramController.instances[
                update.message.chat_id].action(update.message)

    def __getstate__(self):
        return (self.chat_id, self.game)

    def __setstate__(self, state):
        self.chat_id, self.game = state
        self.game.controller = self
