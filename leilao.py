from itemleilao import ItemLeilao
from datetime import datetime


class Leilao():

    def __init__(self, id, dataInicioLeilao, horaInicioLeilao, dataFinalLeilao, horaFinalLeilao):
        self.id = id
        self.dataInicioLeilao = dataInicioLeilao
        self.horaInicioLeilao = horaInicioLeilao
        self.dataFinalLeilao = dataFinalLeilao
        self.horaFinalLeilao = horaFinalLeilao
        self.itemleilao = []

    def inserirItem(self, tituloItem, descricaoItem, lanceMinimoItem, itemArrematado):
        self.itemleilao.append(ItemLeilao(tituloItem, descricaoItem, lanceMinimoItem, itemArrematado))

    def consultarLeilao(rolLeilao, id):
        for id in rolLeilao:
            print(f'_________ INFORMAÇÕES DO LEILAO {id}_________')
            print(f'data inicio: {rolLeilao[id].dataInicioLeilao} | hora inicio: {rolLeilao[id].horaInicioLeilao}')
            print(f'data final: {rolLeilao[id].dataFinalLeilao} | hora final: {rolLeilao[id].horaFinalLeilao}')
            print()
            print(f'____________ ITENS DO LEILAO {id}___________')
            for item in rolLeilao[id].itemleilao:
                print(f'Titulo: {item.tituloItem}')
                print()

    def iniciarLeilao(self): 
        comeco = self.dataInicioLeilao + ' ' + self.horaInicioLeilao

        if datetime.strptime(comeco, '%d/%m/%Y %H:%M') <= datetime.now():
            if len(self.itemleilao) > 0:
                return True
            else:
                return False
        else:
            return False
        

    def finalizarLeilao(self):
        final = self.dataFinalLeilao + ' ' + self.horaFinalLeilao

        if datetime.strptime(final, '%d/%m/%Y %H:%M') <= datetime.now():
            return True
        else:
            return False
