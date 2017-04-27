from datetime import datetime
import pytz


def retornarDiaDaSemana():
    dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira',
            'Sexta-feira', 'Sábado', 'Domingo')
    return dias[datetime.today().weekday()]


def retornarHora():
    date = datetime.now(pytz.timezone('Brazil/East'))
    return '{}:{}h'.format(date.hour, date.minute)


def ObterListaAdmin(bot, chat_id):
    return [admin.user.id for admin in bot.getChatAdministrators(chat_id)]


def VerificarAdmin(bot, update):
    if update.message.chat.type == "private":
        return True
    else:
        if (update.message.from_user.id in
                ObterListaAdmin(bot, update.message.chat_id)):
            return True
    return False


def VerificaSePodeDecretar(usuarioEhAdmin):
    if ((bool(usuarioEhAdmin) or (datetime.today().weekday() == 4 and
                                  int(datetime.today().hour) >= 18))):
        return True
