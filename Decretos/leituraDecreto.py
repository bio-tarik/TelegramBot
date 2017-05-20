import random
import codecs
import Helpers


def obterFrasesDoArquivo():
    data = Helpers.abrirArquivo('DecretoDB.ddg')
    return data["decretos"]


def sortearFrases(frases, quantidade):
    datasComemorativas = [d for d in frases if d['data'] != ""]
    registrosUnicos = [d['frases'] for d in frases if d['data'] == "" and d['unico'] == "True"]
    demaisRegistros = [d['frases'] for d in frases if d['data'] == "" and d['unico'] != "True"]
    retorno = []

    retorno += Helpers.MesclarMultiplosArrays([item['frases'] for item in datasComemorativas if Helpers.VerificarFeriado(item['data'])])
    retorno += Helpers.MesclarMultiplosArrays(demaisRegistros)

    retorno = random.sample(retorno, quantidade - len(registrosUnicos))

    retorno += Helpers.MesclarMultiplosArrays([random.sample(item, 1) for item in registrosUnicos])

    return retorno


def addFrases(frase):
    data = abrirArquivo()
    data["decretos"].append(frase)

    with codecs.open('DecretoDB.ddg', mode='w', encoding='utf-8') as data_file:
        json.dump(data, data_file, ensure_ascii=False)


def manipularMensagem(mensagem):
    return ' '.join(map(str.strip, mensagem))


def formatarMensagem(frases):
    retorno = []
    retorno.append('{} - {}'.format(Helpers.retornarDiaDaSemana(),
                                    Helpers.retornarHora()))
    retorno.append('horário de Brasília. Já pode:\n\n')
    retorno.extend(frases)
    retorno.append('\n\nDecreto liberado. Cumpra-se\n\n#decreto')

    return ' '.join(retorno)
