# -*- coding: utf-8 -*-

class Um():

    # -- Método imprime idade -- #
    @staticmethod
    def imprime_idade(idade):
        idade_anos = idade / 365.00
        idade_meses = idade / 30.00
        idade_dias = idade
        print '------------------------------------------'
        print '-> Idade em [Anos]..: %.2f' % idade_anos
        print '-> Idade em [Meses].: %.2f' % idade_meses
        print '-> Idade em [Dias]..: %.2f' % idade_dias

    # -- Método inicia atividade 01 -- #
    @staticmethod
    def executa():
        print '------------------------------------------'
        print 'ATIVIDADE 01 - IDADE EM ANOS, MESES E DIAS'
        print '-----------  PYTHON 2.7  -----------------'
        print '------------------------------------------'
        print 'INFORME A SUA IDADE (EM DIAS): ',
        idade = int(input())
        Um.imprime_idade(idade)