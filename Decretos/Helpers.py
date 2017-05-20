from datetime import datetime
import pytz


def dateTimeComTZ():
    return datetime.now(pytz.timezone('Brazil/East'))


def retornarDiaDaSemana():
    dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira',
            'Sexta-feira', 'Sábado', 'Domingo')
    return dias[dateTimeComTZ().weekday()]


def retornarHora():
    date = dateTimeComTZ()
    return '{}:{:02d}h'.format(date.hour, date.minute)


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
    if ((bool(usuarioEhAdmin) or (dateTimeComTZ().weekday() == 4 and
                                  int(dateTimeComTZ().hour) >= 18))):
        return True
