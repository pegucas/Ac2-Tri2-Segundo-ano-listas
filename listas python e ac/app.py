from menu import Menu
from functions import Cadastro, Cadastrados, relatorioCompleto, PesquisaJogador, AlterarInfo, Remover, Estatisticas

EscolhaMenu = 0

while EscolhaMenu != 8:
    Menu()

    EscolhaMenu = int(input("Qual sera a opção?: "))

    if EscolhaMenu == 1:
        print("-" * 45)
        print("OK")
        Cadastro()
    elif EscolhaMenu == 2:
        print("-" * 45)
        print("Beleza")
        Cadastrados()
    elif EscolhaMenu == 3:
        print("-" * 45)
        print("joia")
        relatorioCompleto()
    elif EscolhaMenu == 4:
        print("-" * 45)
        print("Ta")
        PesquisaJogador()
    elif EscolhaMenu == 5:
        print("-" * 45)
        print("Kay")
        AlterarInfo()
    elif EscolhaMenu == 6:
        print("-" * 45)
        print("Ta bom")
        Remover()
    elif EscolhaMenu == 7:
        print("-" * 45)
        print("Sim")
        Estatisticas()
    else:
        print("-" * 45)
        print("Encerrando programa...")
