from entidade.molde import Molde
from limite.tela_molde import TelaMolde


class ControladorMolde():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__moldes = []
        self.__tela_molde = TelaMolde()
    
    def incluir_molde(self):
        codigo, material = self.__tela_molde.pega_dados_molde()
        for molde in self.__moldes:
            if (molde.codigo == codigo):
                print("Molde já existe")
        self.__moldes.append(Molde(codigo, material))
    
    def alterar_molde(self):
        self.lista_moldes()
        codigo = self.__tela_molde.seleciona_molde()
        molde = self.consultar_molde(codigo)
        if (molde is not None):
            novo_codigo, novo_material = self.__tela_molde.pega_novos_dados_molde()
            molde.codigo = novo_codigo
            molde.material = novo_material
            self.lista_moldes()
        else:
            self.__tela_molde.mostra_mensagem("MOLDE NÃO EXISTE!")
    
    def consultar_molde(self, codigo: int):
        for molde in self.__moldes:
            if (molde.codigo == codigo):
                return molde
        return None
    
    def lista_moldes(self):
        self.__tela_molde.mostra_mensagem("---Lista de Moldes---")
        for molde in self.__moldes:
            self.__tela_molde.mostra_molde(molde)
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        opcoes = {1: self.incluir_molde,
                2: self.alterar_molde,
                3: self.lista_moldes,
                0: self.retornar
        }

        while True:
            opcoes[self.__tela_molde.mostra_menu()]()