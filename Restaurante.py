
class Restaurante:
    def __init__(self, nome_restaurante, categoria):
        self.nome_restaurante = nome_restaurante
        self.categoria = categoria
        self._ativo = False

    def get_nome(self): 
        return self.nome_restaurante
    
    def get_categoria(self):
        return self.categoria
    
    def get_ativo(self): 
        return self._ativo


    def  ativar_restaurante(self):
        self._ativo = True

    def  desativar_restaurante(self):
        self._ativo = False


    def exibir_restaurante(self):
        print(self.nome_restaurante, self.categoria, self._ativo)


