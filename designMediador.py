class TorreDeControle:
    def __init__(self):
        self.avioes = []

    def adicionar_aviao(self, aviao):
        self.avioes.append(aviao)
        aviao.registrar_torre(self)

    def enviar_mensagem(self, aviao, mensagem):
        print(f'Torre de controle para {aviao.nome}: {mensagem}')
        for outro_aviao in self.avioes:
            if outro_aviao != aviao:
                outro_aviao.receber_mensagem(aviao, mensagem)


class Aviao:
    def __init__(self, nome):
        self.nome = nome
        self.torre = None

    def registrar_torre(self, torre):
        self.torre = torre

    def enviar_mensagem(self, mensagem):
        self.torre.enviar_mensagem(self, mensagem)

    def receber_mensagem(self, aviao, mensagem):
        print(f'{self.nome} recebeu uma mensagem de {aviao.nome}: {mensagem}')


# Criando Torre de Controle
torre_de_controle = TorreDeControle()

# Criando Aviões
aviao1 = Aviao('Aviao 1')
aviao2 = Aviao('Aviao 2')
aviao3 = Aviao('Aviao 3')

# Adicionando Aviões à Torre
torre_de_controle.adicionar_aviao(aviao1)
torre_de_controle.adicionar_aviao(aviao2)
torre_de_controle.adicionar_aviao(aviao3)

# Enviando as mensagens
aviao1.enviar_mensagem('Vamos decolar')
aviao2.enviar_mensagem('Confirmando, para decolar')
aviao3.enviar_mensagem('Aguardando autorização para decolar')

