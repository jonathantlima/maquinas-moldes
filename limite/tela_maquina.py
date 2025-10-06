class TelaMaquina():


    def mostra_menu(self):

        print("-------- MÁQUINAS ----------")
        print("Selecione uma opção")
        print("1 - Incluir máquina")
        print("2 - Alterar máquina")
        print("3 - Listar máquina")
        print("0 - Retornar")
        
        opcao = int(input("Digite sua opção: "))

        return opcao
    
    def coleta_dados_maquina(self):
        print("----- COLETA DE DADOS DA MÁQUINA -----")
        codigo_maquina = int(input("Código da máquina: "))
        codigo_molde = int(input("Código do molde: "))

        return codigo_maquina, codigo_molde
    
    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def exibe_maquina(self, maquina):
        print("CÓDIGO DA MÁQUINA: ", maquina.codigo)
        print("CÓDIGO DO MOLDE DA MÁQUINA: ", maquina.molde.codigo)
        print("MATERIAL DO MOLDE: ", maquina.molde.material)
    
    def seleciona_maquina(self):
        codigo_maquina = int(input("Digite o código da máquina: "))
        return codigo_maquina
    
