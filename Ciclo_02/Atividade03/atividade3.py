# -*- coding: utf-8 -*-

class Tres():

    # -- Método menor_de_tres -- #
    @staticmethod
    def menor_de_tres(n1,n2,n3):
        if (n1 < n2) and (n1 < n3):
            menor = n1
        elif (n2 < n1) and (n2 < n3):
            menor = n2
        elif (n3 < n1) and (n3 < n2):
            menor = n3
        elif (n1 <= n2) or (n1 <= n3):
            menor = n1
        elif (n2 <= n1) or (n2 <= n3):
            menor = n2
        else:
            menor = n3
        return menor

    # -- Método inicia atividade 03 -- #
    @staticmethod
    def executa():
        print '------------------------------------------'
        print '---- ATIVIDADE 03 - MENOR DOS TRÊS     ---'
        print '-----------  PYTHON 2.7  -----------------'
        print '------------------------------------------'
        print 'INFORME UM VALOR (INTEIRO) PARA [N1]: ',
        n1 = int(input())
        print 'INFORME UM VALOR (INTEIRO) PARA [N2]: ',
        n2 = int(input())
        print 'INFORME UM VALOR (INTEIRO) PARA [N3]: ',
        n3 = int(input())
        menor = Tres.menor_de_tres(n1,n2,n3)
        print '-> %d É O MENOR' %menor