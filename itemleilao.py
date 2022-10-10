class ItemLeilao():
    
    def __init__(self, tituloItem, descricaoItem, lanceMinimoItem, itemArrematado):
        self.tituloItem = tituloItem
        self.descricaoItem = descricaoItem
        self.lanceMinimoItem = lanceMinimoItem
        self.itemArrematado = itemArrematado
    
    def consultarItem(self):
        print(f'_______ DADOS DO ITEM {self.tituloItem} _______')
        print(f'Descrição: {self.descricaoItem}\nLance Min: {self.lanceMinimoItem}\nArrematado: {self.itemArrematado}\n')

    def arrematarItem(self, rolLances):
        maiorLance = 0
        idParticipante = ['']

        for lance in rolLances:
            if self.tituloItem == rolLances[lance][2]:
                if lance == 0:
                    maiorLance = rolLances[lance][3]
                    idParticipante[0] = rolLances[lance][0]

                elif maiorLance < rolLances[lance][3]:
                    maiorLance = rolLances[lance][3]
                    idParticipante[0] = rolLances[lance][0]

                self.itemArrematado = True

        return idParticipante[0] , maiorLance
        