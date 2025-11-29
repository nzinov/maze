import argparse
import logging
from telegram_controller import TelegramController

parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true')
parser.add_argument('--do_pickle', action='store_true')
args = parser.parse_args()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TelegramController.debug = args.debug
TelegramController.do_pickle = args.do_pickle
TelegramController.wait()
