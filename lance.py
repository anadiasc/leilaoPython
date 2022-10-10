class Lance():
    def __init__(self, id, valorLance, horaLance):
        self.id = id
        self.valorLance = valorLance
        self.horaLance = horaLance
    
    def registrarLance(self, rolLance, idParticipante, idLeilao, idItem):
        rolLance[self.id] = [idParticipante, idLeilao, idItem, self.valorLance, self.horaLance]
