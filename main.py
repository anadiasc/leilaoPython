from participante import Participante 
from leilao import Leilao
from lance import Lance
from datetime import datetime


rolParticipantes = {

}

rolLeilao = {

}

lances = {

}


def addLeilao(rolLeilao, leilao):
    rolLeilao.__setitem__(leilao.id, leilao)


leilao1 = Leilao(1, '09/10/2022', '11:20', '09/10/2022', '22:04')
leilao1.inserirItem('anel', 'ouro', 100.00, False)
leilao1.inserirItem('colar', 'prata', 50.00, False)
leilao1.inserirItem('tiara', 'dimante', 1000.00, False)

addLeilao(rolLeilao, leilao1)


while True:
    print('Bem-vindo ao Lance Certo!\n')
    
    if leilao1.finalizarLeilao() == True:
        print('____________________________________________________')
        print(f'o leiao {leilao1.id} foi finalizado')
        for item in leilao1.itemleilao:
            arrematar = item.arrematarItem(lances)
            if item.itemArrematado == True:
                print(f'O item {item.tituloItem} foi arrematado! \nO novo dono é {arrematar[0]} e o valor do lance foi {arrematar[1]}')     
        print('____________________________________________________')

    print('Menu opções:\n1. login\n2. cadastro')

    escolha = int(input('insira a opção desejada: '))

    if escolha == 1:
        login = input('login: ')
        senha = input('senha: ')
        realizarLogin = Participante.logindoParticipante(rolParticipantes, login, senha)

        if realizarLogin == True: 

            for leilao in rolLeilao:
                if rolLeilao[leilao].iniciarLeilao() == True and rolLeilao[leilao].finalizarLeilao() == False:
                    print('______________________________________')
                    print(f'Id Leilão disponivel: {leilao}')
                    print('______________________________________')

            while True:
                print(f'Olá, {login}!')
                print('O que deseja?\n1. consultar leilao\n2. ofertar lance\n3. sair\n')
                
                op = int(input('insira a opção: '))

                if op == 1:
                    idConsulta = input('id do leilao: ')
                    Leilao.consultarLeilao(rolLeilao, idConsulta)

                elif op == 2:
                    idLance = input('Informe um id para seu lance: ')
                    idLeilao = int(input('Id do Leilao: '))

                    for item in rolLeilao[idLeilao].itemleilao:
                        item.consultarItem()

                    itemDesejado = input('Titulo do item: ')

                    for item in rolLeilao[idLeilao].itemleilao:
                        if itemDesejado in item.tituloItem:

                            if item.itemArrematado == False:
                                valorLance = float(input('Valor do lance: '))
                                hora = datetime.time(datetime.now())

                                if valorLance >= item.lanceMinimoItem:
                                    lance1 = Lance(idLance, valorLance, hora)
                                    lance1.registrarLance(lances, login, idLeilao, itemDesejado)
                                    print('Lance ofertado!\n')
                                else:
                                    print('valor do lance inferior ao lance minimo')
                            else:
                                print('item já arrematado')

                elif op == 3:
                    print('saindo...\n')
                    break

    elif escolha == 2:
        print('________________CADASTRO________________')
        nome = input('Nome: ')
        login = input('Login: ')
        senha = input('Senha: ')
        email = input('Email: ')
        endereco = input('Endereco: ')
        telefone = input('Telefone: ')
        print('_________________________________________')
        Participante.registrarParticipante(rolParticipantes, nome, login, senha, email, endereco, telefone)

    else:
        print('escolha invalida')
    