# exec(open(leituraDecreto.py).read())
import json, random, codecs
import os

def abrirArquivo():
    with open(os.path.join(os.path.dirname(__file__), 'DecretoDB.ddg')) as data_file:
        data = json.load(data_file)
    return data

def obterFrases():
    data = abrirArquivo()

    return data["decretos"]

def sortearFrases(frases):
    return random.sample(frases, 5)

def addFrases(frase):
    data = abrirArquivo()
    data[decretos].append(frase)

    with codecs.open('DecretoDB.ddg', mode='w', encoding='utf-8') as data_file:
        json.dump(data, data_file, ensure_ascii=False)

def manipularMensagem(mensagem):
    return ' '.join(map(str.strip, mensagem))


