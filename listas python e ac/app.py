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
    elif EscolhaMenu == 8:
        print("-" * 45)
        print("Encerrando programa...")
        break
    elif EscolhaMenu == 0:
        print("Teste de racismo \nEm um galinheiro existem 30 galinhas. Um crioulo levou 10 galinhas. Quantas galinhas ficaram no galinheiro ? \nRESULTADO ABAIXO: \nSe você respondeu 20 galinhas - Você é racista. \nSe você respondeu 40 galinhas - Parabéns !! \nSe tinham 30 e ele levou mais 10, ficaram 40 galinhas. Ninguém falou que ele roubou 10.")
    else:
        print("É tão dificil assim escolher de 1 a 8?")
