from limite.tela_sistema import TelaSistema
from controle.controlador_molde import ControladorMolde
from controle.controlador_maquina import ControladorMaquina


class ControladorSistema:

    def __init__(self):
        self.__controlador_molde = ControladorMolde(self)
        self.__controlador_maquina = ControladorMaquina(self)
        self.__tela_sistema = TelaSistema()
    
    @property
    def controlador_molde(self):
        return self.__controlador_molde
    
    @property
    def controlador_maquina(self):
        return self.__controlador_maquina
    
    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_molde(self):
        self.__controlador_molde.abre_tela()
    
    def cadastrar_maquina(self):
        self.__controlador_maquina.abre_tela()
    
    def encerra_sistema(self):
        exit(0)
    
    def abre_tela(self):
        opcoes = {1: self.cadastra_molde,
                  2: self.cadastrar_maquina,
                  0: self.encerra_sistema}
        
        while True:
            opcao = self.__tela_sistema.menu()
            opcoes[opcao]()