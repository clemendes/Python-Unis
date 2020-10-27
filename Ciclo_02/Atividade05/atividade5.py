# -*- coding: utf-8 -*-

class Cinco():

    # Função inverte palavras #
    @staticmethod
    def inverter_palavras(frase):
        txt_invertido = ''
        for palavra in frase.split(' '):
            txt_invertido += palavra[::-1]+' '

        print(txt_invertido)

    # -- Método inicia atividade 05 -- #
    @staticmethod
    def executa():
        print '------------------------------------------'
        print '---- ATIVIDADE 05 - PALAVRAS INVERTIDAS --'
        print '-----------  PYTHON 2.7  -----------------'
        print '------------------------------------------'
        print 'DIGITE UMA FRASE: ',
        txt = raw_input()
        Cinco.inverter_palavras(txt)