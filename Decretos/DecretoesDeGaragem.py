import leituraDecreto as frases
import Helpers
from telegram.ext import Updater, CommandHandler
import logging

# Enable logging
logging.basicConfig(format=('%(asctime)s - %(name)s -'
                            '%(levelname)s - %(message)s'), level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text('Bem vindo ao Decretoes de Garagem bot. '
                              'Meu objetivo é trazer alegria '
                              'responsável (ou não) aos membros do '
                              'melhor grupo.\n\n'
                              'Caso não saiba o que fazer, NÃO ENTRE '
                              'EM PÂNICO e digite /help')


def help(bot, update):
    update.message.reply_text('É sexta-feira? 18h00? Está com sede e com o '
                              'copo na mão? Só falta a permissão? '
                              'Então digite /decretar !')


def decretar(bot, update):
    if Helpers.VerificaSePodeDecretar(Helpers.VerificarAdmin(bot, update)):
        conteudo = frases.sortearFrases(frases.obterFrasesDoArquivo(), 10)
        decreto = frases.formatarMensagem(conteudo)
        update.message.reply_text(decreto)
    else:
        update.message.reply_text('Oloko, ainda não é hora de decretar! '
                                  'Solicite um decreto extraordinário ao '
                                  'dragão mais próximo.')

'''
def adicionar(bot, update, args):
    if len(args) > 0:
        frases.addFrases(frases.manipularMensagem(args))
        update.message.reply_text('Adicionado')
    else:
        update.message.reply_text('Este comando deve vir acompanhado da '
                                  'mensagem a ser adicionada (Por exemplo: '
                                  '/adicionar Liberado beber chopp Kaiser)')
'''


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    updater = Updater('')

    updater.dispatcher.add_handler(
        CommandHandler('start', start))
    updater.dispatcher.add_handler(
        CommandHandler('help', help))
    updater.dispatcher.add_handler(
        CommandHandler('decretar', decretar))
    '''
    updater.dispatcher.add_handler(
        CommandHandler('adicionar', adicionar, pass_args=True))
    '''
    updater.dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
