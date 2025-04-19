
class Parametros:
    def __init__(self):
        
        # Configurações da janela
        self.janela_largura = 1280                      # Pixels
        self.janela_altura = 720                        # Pixels
        self.janela_titulo = "Flappy Dragon"            # Título da janela

        # Variáveis de física
        self.valor_gravidade = -9.80665 /2                # Aceleração da gravidade (m/s²)
        self.valor_velocidade_pulo = 1                # Velocidade do pulo (em relação à altura da janela por segundo)

        # Configurações do personagem
        self.personagem_posicao_horizontal = -0.45      # Posição horizontal do personagem (em relação à largura da janela)
        self.personagem_largura = 0.15                  # Largura do personagem (em relação à largura da janela)
        self.personagem_altura = 0.225                  # Altura do personagem (em relação à altura da janela)
        self.personagem_vidas = 3                       # Número de vidas do personagem
        self.personagem_pontos = 0                      # Pontos do personagem
        self.personagem_duracao_invencibilidade = 3     # Duração da invencibilidade (em segundos)

        # Configurações do obstáculo (torre)
        self.torre_tempo_1a_geracao = 0.5               # Tempo para gerar o 1º obstáculo (em segundos)
        self.torre_tempo_entre_geracao = 3              # Tempo entre a geração de obstáculos (em segundos)
        self.torre_velocidade_movimento = 0.2           # Velocidade dos obstáculos (em relação à largura da janela por segundo)
        self.torre_altura_do_gap = 0.5                  # Altura do espaço entre os obstáculos (em relação à altura da janela)
        self.torre_largura = 0.23                       # Largura dos obstáculos (em relação à largura da janela)
        self.torre_altura = 1.35                        # Altura máxima dos obstáculos (em relação à altura da janela)
