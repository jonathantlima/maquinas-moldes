class TelaMolde():


    def mostra_menu(self):

        print("-------- MOLDES ----------")
        print("1 - Incluir molde")
        print("2 - Alterar molde")
        print("3 - Listar moldes")
        print("4 - Consultar molde")
        print("0 - Retornar")
        
        opcao = int(input("Selecione uma opção: "))

        return opcao
    
    def pega_dados_molde(self):
        print("----- Coleta de Dados -----")
        codigo = int(input("Digite o código do molde: "))
        material = input("Digite o 'material' do molde: ")

        return codigo, material
    
    def pega_novos_dados_molde(self):
        print("----- Coleta de Novos Dados -----")
        codigo = int(input("Digite o novo código do molde: "))
        material = input("Digite o novo 'material' do molde: ")

        return codigo, material
    
    def mostra_molde(self, molde):
        print("CÓDIGO DO MOLDE: ", molde.codigo)
        print("MATERIAL DO MOLDE: ", molde.material)
        print("\n")

    def seleciona_molde(self):
        codigo = int(input("Código do molde desejado: "))
        return codigo
    
    def mostra_mensagem(self, mensagem):
        print(mensagem)