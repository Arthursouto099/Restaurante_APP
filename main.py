from Restaurante import Restaurante
from app import App
import os

app = App()

def criar_restaurante():
    nome_restaurante = input('Digite o nome do Resturante: ')
    categoria = input('Digite a categoria do Restaurante: ')

    restaurante = Restaurante(nome_restaurante, categoria)

    app.adicionar_restaurante(restaurante)

    print(f'O restaurante {nome_restaurante} foi adicionado com sucesso!')    

    pergunta_cliente = input(f'Você ja deseja ativar o restaurante: {nome_restaurante}? ').upper()

    if(pergunta_cliente == 'SIM'):
        restaurante.ativar_restaurante()
        print('Restaurante ativado com sucesso')
    else:
        print('Ok, ative em outro momento!')

def ativar_restaurante():
      nome_restaurante = input('Digite o nome do Resturante: ')

      app.ativar_restaurante(nome_restaurante)

def desativar_restaurante():
      nome_restaurante = input('Digite o nome do Resturante: ')

      app.desativar_restaurante(nome_restaurante)




    

def mostrar_opcoes(): 
    print("""
    
░█████╗░░█████╗░██████╗░██████╗░░█████╗░██████╗░██╗░█████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗╚██╗██╔╝
██║░░╚═╝███████║██████╔╝██║░░██║███████║██████╔╝██║██║░░██║░╚███╔╝░
██║░░██╗██╔══██║██╔══██╗██║░░██║██╔══██║██╔═══╝░██║██║░░██║░██╔██╗░
╚█████╔╝██║░░██║██║░░██║██████╔╝██║░░██║██║░░░░░██║╚█████╔╝██╔╝╚██╗
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝
""")
    
    print('Opção --> 1: Cadastrar Restaurante')
    print('Opção --> 2: listar Restaurantes')
    print('Opção --> 3: Ativar Restaurante')
    print('Opção --> 4: Desativar Restaurante')
    print('Opção --> 5: Sair\n')

    




def iniciar_programa():
    mostrar_opcoes()

    pergunta_usuario = int(input('Escolha uma Opção: '))


    if pergunta_usuario == 1:
        criar_restaurante()
        input('Clique qualquer tecla para voltar ao menu: ')
        os.system('cls')
        iniciar_programa()

    elif pergunta_usuario == 2:
        app.listar_restaurantes()
        input('Clique qualquer tecla para voltar ao menu: ')
        os.system('cls')
        iniciar_programa()

    elif pergunta_usuario == 3:  
        ativar_restaurante()
        input('Clique qualquer tecla para voltar ao menu: ')
        os.system('cls')
        iniciar_programa()
    

    elif pergunta_usuario == 4:  
        desativar_restaurante()
        input('Clique qualquer tecla para voltar ao menu: ')
        os.system('cls')
        iniciar_programa()
            

    elif pergunta_usuario == 5:
        os.system('cls')
        print('finalizando app...')
        

def main():
    iniciar_programa()

if __name__ ==  '__main__':
    main()