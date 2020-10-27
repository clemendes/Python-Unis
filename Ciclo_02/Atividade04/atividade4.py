# -*- coding: utf-8 -*-

class Quatro():

    # Função eh_numero_primo #
    @staticmethod
    def eh_numero_primo(n):
        cont = 0
        for i in range(1, n+1, 1):
            if n % i == 0:
                cont += 1
                if cont > 2:
                    return False
                    break

        if cont == 2:
            return True

    # -- Método inicia atividade 04 -- #
    @staticmethod
    def executa():
        print '------------------------------------------'
        print '---- ATIVIDADE 04 - NUMEROS PRIMOS     ---'
        print '---- NUMEROS PRIMOS DE 1 A 100 -----------'
        print '-----------  PYTHON 2.7  -----------------'
        print '------------------------------------------'
        for i in range(1,101,1):
            if i == 1:
                continue
            else:
                print '[%d]: ' %i, Quatro.eh_numero_primo(i)