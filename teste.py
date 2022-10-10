class Item():
    def __init__(self, nomeItem) -> None:
        self.nomeItem = nomeItem

    def arrematarItem(self, rolLances): #retorna True ou False
        maiorLance = 0
        idParticipante = ['']
        for lance in rolLances:
            if self.nomeItem == rolLances[lance][2]:
                if lance == 0:
                    maiorLance = rolLances[lance][3]
                    idParticipante[0] = rolLances[lance][0]

                elif maiorLance < rolLances[lance][3]:
                    maiorLance = rolLances[lance][3]
                    idParticipante[0] = rolLances[lance][0]

        print(maiorLance)
        print(idParticipante)

class Lance():
    def __init__(self, id, valorLance, horaLance):
        self.id = id
        self.valorLance = valorLance
        self.horaLance = horaLance
    
    def registrarLance(self, rolLance, idParticipante, idLeilao, idItem):
        rolLance[self.id] = [idParticipante, idLeilao, idItem, self.valorLance, self.horaLance]

lances = {

}

item1 = Item('anel')

lance1 = Lance(1, 100, '11: 40')
lance2 = Lance(2, 100, '11: 40')
lance3 = Lance(3, 400, '11: 40')
lance4 = Lance(4, 500, '11: 40')

lance1.registrarLance(lances, 'ana', 1, 'anel')
lance2.registrarLance(lances, 'jose', 1, 'anel')
lance3.registrarLance(lances, 'leo', 1, 'anel')
lance4.registrarLance(lances, 'ray', 1, 'tiara')

item1.arrematarItem(lances)