from datetime import datetime
import pytz

def retornarDiaDaSemana():
    dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
    return dias[datetime.today().weekday()]

def retornarHora():
    date = datetime.now(pytz.timezone('Brazil/East'))
    return '{}:{}h'.format(date.hour, date.minute)