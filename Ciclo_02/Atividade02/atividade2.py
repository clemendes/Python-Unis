# -*- coding: utf-8 -*-

class Dois():

    # -- Método calcula area -- #
    @staticmethod
    def calcula_area(a,b,c):
        if ((a + b) < c) or ((a + c) < b) or ((b + c) < a):
            print '-> OS LADOS ', a, b, c, ' NÃO FORMAM UM TRIÂNGULO!'
        else:
            # Fórmula de Heron
            # Calcular o Semi-Perimetro
            sp = (a + b + c) / 2
            # Calcular a Área
            area = (sp * (sp - a) * (sp - b) * (sp - c)) ** 0.5
            print '-> ÁREA DO TRIÂNGULO = %.2f' %area

    # -- Método inicia atividade 02 -- #
    @staticmethod
    def executa():
        print '------------------------------------------'
        print '--- ATIVIDADE 02 - ÁREA DO TRIÂNGULO -----'
        print '-----------  PYTHON 2.7  -----------------'
        print '------------------------------------------'
        print 'INFORME UM VALOR (INTEIRO) PARA [A]: ',
        a = int(input())
        print 'INFORME UM VALOR (INTEIRO) PARA [B]: ',
        b = int(input())
        print 'INFORME UM VALOR (INTEIRO) PARA [C]: ',
        c = int(input())
        Dois.calcula_area(a, b, c)