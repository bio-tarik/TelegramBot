import leituraDecreto as frases
from telegram.ext import Updater, CommandHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)



def start(bot, update):
    update.message.reply_text('Hello World!')

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def decretar(bot, update):
    update.message.reply_text(
        frases.sortearFrases(frases.obterFrases()))

def adicionar(bot, update, args):
    if len(args) > 0:
        frases.addFrases(frases.manipularMensagem(args))
        update.message.reply_text('Adicionado')
    else:
        update.message.reply_text("no args")

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    updater = Updater('')

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(CommandHandler('decretar', decretar))
    updater.dispatcher.add_handler(CommandHandler('adicionar', adicionar, pass_args=True))
    updater.dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
