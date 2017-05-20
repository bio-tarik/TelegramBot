from datetime import datetime, timedelta
import os
import json
import pytz


def abrirArquivo(nome):
    with open(os.path.join(os.path.dirname('__file__'),
                           nome)) as data_file:
        data = json.load(data_file)
    return data


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


def MesclarMultiplosArrays(arrays):
    retorno = [item for sublist in arrays for item in sublist]
    return retorno

Feriados = abrirArquivo('Feriados.ddg')['feriados']


def VerificarFeriado():
    retorno = []
    for x in range(0, len(Feriados)):
        if Feriados[x]['data'] != "":
            registroFeriado = datetime.strptime(
                Feriados[x]['data'] + '/' + str(datetime.now().year),
                '%d/%m/%Y')
            limiteInferiorRegistro = registroFeriado - timedelta(6)
            # verifica se o feriado ocorre nesta semana
            if (registroFeriado.date() >= datetime.now().date() and
                    limiteInferiorRegistro.date() <= datetime.now().date()):
                retorno.append(Feriados[x]['nome'])
        else:
            pass
    return retorno

print(VerificarFeriado())
