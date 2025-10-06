from entidade.molde import Molde

class Maquina():

    def __init__(self, codigo_maquina: int, molde: Molde):
        self.__codigo = codigo_maquina
        self.__molde = molde
    
    @property
    def codigo(self) -> int:
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo_maquina: int):
        if isinstance(codigo_maquina, int):
            self.__codigo = codigo_maquina
    
    @property
    def molde(self) -> Molde:
        return self.__molde
    
    @molde.setter
    def molde(self, molde: Molde):
        if isinstance(molde, Molde):
            self.__molde = molde