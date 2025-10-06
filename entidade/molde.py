class Molde():

    def __init__(self, codigo_molde: int, material: str):
        self.__codigo = codigo_molde
        self.__material = material

    @property
    def codigo(self) -> int:
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo_molde: int):
        if isinstance(codigo_molde, int):
            self.__codigo = codigo_molde
    
    @property
    def material(self) -> str:
        return self.__material
    
    @material.setter
    def material(self, material: str):
        if isinstance(material, str):
            self.__material = material
