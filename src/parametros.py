# Classe armazena os parâmetros do jogo como variáveis da mesma. 
# Evita-se o uso de dicionário para obter melhor performance.

class Parametros:
    def __init__(self):
        
        # Configurações da janela
        self.janela_largura = 1280                      # Pixels
        self.janela_altura = 720                        # Pixels
        self.janela_titulo = "Flappy Dragon"            # Título da janela

        # Variáveis de física
        self.valor_gravidade = -4                       # Aceleração da gravidade fictícia, nesse jogo (m/s²)
        self.valor_velocidade_pulo = 1                  # Velocidade do pulo (em relação à altura da janela por segundo)
        self.valor_velocidade_objetos = 0.2             # Velocidade das torres e powerups (em relação à largura da janela por segundo)

        # Configurações do personagem
        self.personagem_posicao_horizontal = -0.45      # Posição horizontal do personagem (em relação à largura da janela)
        self.personagem_largura = 0.10                  # Largura do personagem (em relação à largura da janela)
        self.personagem_altura = self.personagem_largura * (928 / 857) * (self.janela_largura / self.janela_altura)  # Altura do personagem é calculada mantendo a proporção da imagem original
        self.personagem_vidas = 3                       # Número de vidas do personagem
        self.personagem_pontos = 0                      # Pontos do personagem
        self.personagem_duracao_invencibilidade = 3     # Duração da invencibilidade (em segundos)

        # Configurações do obstáculo (torre)
        self.torre_tempo_1a_geracao = 0.5               # Tempo para gerar o 1º obstáculo (em segundos)
        self.torre_tempo_entre_geracao = 3              # Tempo entre a geração de obstáculos (em segundos)
        self.torre_altura_do_gap = 0.5                  # Altura do espaço entre os obstáculos (em relação à altura da janela)
        self.torre_largura = 0.23                       # Largura dos obstáculos (em relação à largura da janela)
        self.torre_altura = 1.35                        # Altura máxima dos obstáculos (em relação à altura da janela)

        # Configurações do power up
        self.power_up_largura = 0.04                    # Largura do power up (em relação à largura da janela)
        self.power_up_altura = self.power_up_largura * (self.janela_largura / self.janela_altura)  # Altura do power up (em relação à altura da janela)
        self.power_up_tempo_entre_geracao = 20          # A cada janela de 20 segundos, um power up é gerado aleatoriamente
    