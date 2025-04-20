import random
from src.texturas import carregarTextura
from src.parametros import Parametros

class PowerUp:
    # Recebe opcionalmente a lista de torres como parâmetro, para verificar se o power up não colide com nenhuma torre já existente
    def __init__(self, offset_x_geracao = 0):

        # Instancia classe de parâmetros do jogo
        params = Parametros()
        
        # Configurações do Power Up
        self.largura        = params.power_up_largura
        self.altura         = params.power_up_altura
        self.tempo_geracao  = params.power_up_tempo_entre_geracao
        self.velocidade     = params.valor_velocidade_objetos # Velocidade do movimento
        
        # Variáveis para garantir que um par de torres não gere mais que um ponto no jogo
        self.gerou_ponto = False

        # Carrega a imagem com a textura
        self.textura_id = carregarTextura('texturas/power_up.png')

        # Cria uma posição vertical aleatória, após o fim da tela, sem limites verticais
        self.setPosicao(
            1 + self.largura / 2 + offset_x_geracao,  # O offset é usado para gerar o power up após a torre mais a direita, quando necessário
            random.uniform(-1, 1)
        )
            

    # Função que atualiza a posição do power up, recebendo a posição central dele (x e y) e calculando os cantos
    def setPosicao(self, x, y):

        self.canto_inf_esq_x = x - self.largura / 2
        self.canto_inf_esq_y = y - self.altura  / 2
        self.canto_inf_dir_x = x + self.largura / 2
        self.canto_inf_dir_y = y - self.altura  / 2
        self.canto_sup_dir_x = x + self.largura / 2
        self.canto_sup_dir_y = y + self.altura  / 2
        self.canto_sup_esq_x = x - self.largura / 2
        self.canto_sup_esq_y = y + self.altura  / 2
        self.centro_x = x
        self.centro_y = y


    # Faz uma função apenas para movimentar pois é mais eficiente do que recalcular todos os cantos sempre que o power up se movimenta
    def movimentar(self, delta_time):
        
        # Calcula a distância que o power up deve se mover com base na velocidade e no tempo desde o último frame
        delta = self.velocidade * delta_time

        # Atualiza apenas as variáveis X, pois o power up não se movimenta verticalmente
        self.canto_inf_esq_x -= delta
        self.canto_inf_dir_x -= delta
        self.canto_sup_dir_x -= delta
        self.canto_sup_esq_x -= delta
        self.centro_x -= delta

    # Verifica se o personagem colidiu com o power up
    def colidiu_jogador_powerup(self, player) -> bool:
        if player.canto_inf_dir_x >= self.canto_inf_esq_x and player.canto_inf_esq_x <= self.canto_inf_dir_x and player.canto_sup_dir_y >= self.canto_inf_esq_y and player.canto_inf_dir_y <= self.canto_sup_dir_y:
            return True 
        return False
    