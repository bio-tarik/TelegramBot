import json, random, codecs
import os
import Helpers

def abrirArquivo():
    with open(os.path.join(os.path.dirname(__file__), 'DecretoDB.ddg')) as data_file:
        data = json.load(data_file)
    return data

def obterFrasesDoArquivo():
    data = abrirArquivo()
    return data["decretos"]

def sortearFrases(frases, quantidade):
    return random.sample(frases, quantidade)

def addFrases(frase):
    data = abrirArquivo()
    data["decretos"].append(frase)

    with codecs.open('DecretoDB.ddg', mode='w', encoding='utf-8') as data_file:
        json.dump(data, data_file, ensure_ascii=False)

def manipularMensagem(mensagem):
    return ' '.join(map(str.strip, mensagem))

def formatarMensagem(frases):
    retorno = [];
    retorno.append('{} - {}'.format(Helpers.retornarDiaDaSemana(), Helpers.retornarHora()))
    retorno.append('horário de Brasília. Já pode:\n\n')
    retorno.extend(frases)
    retorno.append('\n\nDecreto liberado. Cumpra-se #decreto')
    
    return ' '.join(retorno)
