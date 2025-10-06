from entidade.maquina import Maquina
from limite.tela_maquina import TelaMaquina


class ControladorMaquina():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__maquinas = []
        self.__tela_maquina = TelaMaquina()
    
    def abre_tela(self):
        opcoes = {1: self.incluir_maquina,
                2: self.excluir_maquina,
                3: self.lista_maquinas,
                0: self.retornar
        }

        while True:
            opcoes[self.__tela_maquina.mostra_menu()]()
    
    def incluir_maquina(self):
        self.__controlador_sistema.controlador_molde.lista_moldes()
        codigo_maquina, codigo_molde = self.__tela_maquina.coleta_dados_maquina()

        molde = self.__controlador_sistema.controlador_molde.consultar_molde(codigo_molde)
        if (molde is not None):
            maquina = Maquina(codigo_maquina, molde)
            self.__maquinas.append(maquina)
        else:
            self.__tela_maquina.mostra_mensagem("Erro no cadastro da máquina")
    
    def lista_maquinas(self):
        for maquina in self.__maquinas:
            self.__tela_maquina.exibe_maquina(maquina)
    
    def seleciona_maquina(self, codigo):
        for maquina in self.__maquinas:
            if (maquina.codigo == codigo):
                return maquina
        return None

    def excluir_maquina(self):
        self.lista_maquinas()
        codigo_maquina = self.__tela_maquina.seleciona_maquina()
        maquina = self.seleciona_maquina(codigo_maquina)

        if (maquina is not None):
            self.__maquinas.remove(maquina)
        else:
            self.__tela_maquina.mostra_mensagem("Essa máquina não existe!")
   
    def retornar(self):
        self.__controlador_sistema.abre_tela()