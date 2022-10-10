class Participante():

    def __init__(self, nomeParticipante, loginParticipante, senhaParticipante, emailParticipante, enderecoParticipante, telefoneParticipante):
        self.nomeParticipante = nomeParticipante
        self.loginParticipante = loginParticipante
        self.senhaParticipante = senhaParticipante
        self.emailParticipante = emailParticipante
        self.enderecoParticipante = enderecoParticipante
        self.telefoneParticipante = telefoneParticipante

    def registrarParticipante(rolParticipantes, nomeParticipante, loginParticipante, senhaParticipante, emailParticipante, enderecoParticipante, telefoneParticipante):
        rolParticipantes[loginParticipante] = Participante(nomeParticipante, loginParticipante, senhaParticipante, emailParticipante, enderecoParticipante, telefoneParticipante)
    
        return True

    def logindoParticipante(rolParticipantes, login, senha):
        if login in rolParticipantes:
            if senha == rolParticipantes[login].senhaParticipante:
                return True
            else:
                return False
    