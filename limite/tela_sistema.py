class TelaSistema:

    def menu(self):
        print(">>> SISTEMA DE MÁQUINAS <<<")
        print("Selecione uma opção")
        print("1 - Moldes")
        print("2 - Máquinas")
        print("0 - Finalizar")
    
        opcao = int(input("Selecione uma opção: "))
        return opcao