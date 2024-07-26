from  Restaurante import Restaurante

class App: 
    def __init__(self):
        self.lista_restaurantes = [] 


    def adicionar_restaurante(self, restaurante):
        self.lista_restaurantes.append(restaurante)

    def listar_restaurantes(self):
        for i in self.lista_restaurantes:
            print(f'NOME DO RESTAURANTE: {i.get_nome()}, CATEGORIA: {i.get_categoria()}, ATIVO: {i.get_ativo()}')


    def ativar_restaurante(self, restaurante):
        for i in self.lista_restaurantes:
            if(restaurante == i.get_nome()):
                if(i.get_ativo() == True):
                    print('restaurante ja está ativo')
                else: 
                    i.ativar_restaurante()
                    print('restaurante está sendo ativado')

    def desativar_restaurante(self, restaurante):
        for i in self.lista_restaurantes:
            if(restaurante == i.get_nome()):
                if(i.get_ativo() == False):
                    print('restaurante ja está Desativado')
                else: 
                    i.desativar_restaurante()
                    print('restaurante está sendo Desativado')
        

         
            
         
            
