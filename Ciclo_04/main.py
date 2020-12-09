#-*- coding: utf-8 -*-
from db_api import MyApp
from os import system, name

# --------------------------
#   Atividade Ciclo 04
# --------------------------
#   Aluno: Cleverson Mendes
# --------------------------
#   Versão: Python 3  
# --------------------------

if __name__ == '__main__':

    # Função Limpa Tela
    def clear(): 
        if name == 'nt': 
            _ = system('cls')  
        else: 
            _ = system('clear') 

    # Criando a conexão com o banco.
    App = MyApp()

    opcao_menu = 1
    
    while (opcao_menu != '0'):
        print('--------------------------')
        print('    CALCULADORA DE IMC    ')
        print('--------------------------')
        print('1. Calcular / Registrar')
        print('2. Consultar por ID')
        print('3. Listar Registros')
        print('0. Sair')
        print('--------------------------')
        opcao_menu = input('Digite a opção desejada: ')
        print('--------------------------')
        
        if opcao_menu == '1':
            nome = input('Digite o Nome: ')
            endereco = input('Digite o Endereço: ')
            altura = float(input('Digite a Altura (cm): '))
            peso = float(input('Digite o Peso (Kg): '))
            imc = float(peso) / (float(altura) / 100 * float(altura) / 100)
            imc = float('%.2f' %imc)
            exame = (nome, endereco, altura, peso, imc)
            print(exame)
            # Inserindo um registro tabela.
            App.inserir_registro(exame=exame)
            input('Pressione [ENTER] para continuar...')
            clear()
            
        elif opcao_menu == '2':
            id = int(input('Informe o ID para consulta: '))
            print(App.consultar_registro(rowid=id))
            input('Pressione [ENTER] para continuar...')
            clear()

        elif opcao_menu == '3':
            registros = App.listar_registros()
            for registro in registros:
                print(registro)
            input('Pressione [ENTER] para continuar...')
            clear()
            
        elif (opcao_menu == '0'):
            print('Fim!')

        else:
            print('Opcao invalida!')
            input('Pressione [ENTER] para continuar...')
            clear()
