import random
from src.texturas import carregarTextura
from src.parametros import Parametros

class Torre:
    def __init__(self):

        # Instancia classe de parâmetros do jogo
        params = Parametros()
        
        # Configurações da Torre
        self.largura        = params.get('torre_largura')
        self.altura         = params.get('torre_altura')
        self.altura_do_gap  = params.get('torre_altura_do_gap')
        self.velocidade     = params.get('torre_velocidade_movimento') # Velocidade dos obstáculos
        
        # Carrega a imagem com a textura do personagem
        self.textura_superior_id = carregarTextura('texturas/torre_superior.png')
        self.textura_inferior_id = carregarTextura('texturas/torre_inferior.png')

        # Determina altura máxima do centro do espaço entre os obstáculos
        altura_maxima_centro_gap = -1 + self.altura + self.altura_do_gap / 2

        # Cria uma posição vertical aleatória, dentro dos limites verticais, à direita do fim da tela
        self.setPosicao(
            1 + self.largura / 2, 
            random.uniform(-altura_maxima_centro_gap, altura_maxima_centro_gap)
        )

    # Função que atualiza a posição da torre, recebendo a posição do centro do espaço entre os obstáculos
    def setPosicao(self, x, y):

        # Torre Superior
        self.sup_canto_inf_esq_x = x - self.largura / 2
        self.sup_canto_inf_esq_y = y + self.altura_do_gap / 2
        self.sup_canto_inf_dir_x = x + self.largura / 2
        self.sup_canto_inf_dir_y = y + self.altura_do_gap / 2
        self.sup_canto_sup_dir_x = x + self.largura / 2
        self.sup_canto_sup_dir_y = y + self.altura_do_gap / 2 + self.altura
        self.sup_canto_sup_esq_x = x - self.largura / 2
        self.sup_canto_sup_esq_y = y + self.altura_do_gap / 2 + self.altura
        
        # Torre Inferior
        self.inf_canto_inf_esq_x = x - self.largura / 2
        self.inf_canto_inf_esq_y = y - self.altura_do_gap / 2 - self.altura
        self.inf_canto_inf_dir_x = x + self.largura / 2
        self.inf_canto_inf_dir_y = y - self.altura_do_gap / 2 - self.altura
        self.inf_canto_sup_dir_x = x + self.largura / 2
        self.inf_canto_sup_dir_y = y - self.altura_do_gap / 2
        self.inf_canto_sup_esq_x = x - self.largura / 2
        self.inf_canto_sup_esq_y = y - self.altura_do_gap / 2

    # Faz uma função apenas para movimentar pois é mais eficiente do que recalcular todos os cantos sempre que a torre se movimenta
    def movimentar(self, delta_time):
        
        # Calcula a distância que a torre deve se mover com base na velocidade dos obstáculos e no tempo desde o último frame
        delta = self.velocidade * delta_time

        # Torre Superior
        self.sup_canto_inf_esq_x -= delta
        self.sup_canto_inf_dir_x -= delta
        self.sup_canto_sup_dir_x -= delta
        self.sup_canto_sup_esq_x -= delta

        # Torre Inferior
        self.inf_canto_inf_esq_x -= delta
        self.inf_canto_inf_dir_x -= delta
        self.inf_canto_sup_dir_x -= delta
        self.inf_canto_sup_esq_x -= delta


    # Verifica se o personagem colidiu com alguma das torres
    def colidiu(self, player) -> bool:

        # Torre Superior
        if player.canto_inf_dir_x >= self.sup_canto_inf_esq_x and player.canto_inf_esq_x <= self.sup_canto_inf_dir_x and player.canto_sup_dir_y >= self.sup_canto_inf_esq_y and player.canto_inf_dir_y <= self.sup_canto_sup_dir_y:
            return True 
        
        # Torre Inferior
        if player.canto_inf_dir_x >= self.inf_canto_inf_esq_x and player.canto_inf_esq_x <= self.inf_canto_inf_dir_x and player.canto_sup_dir_y >= self.inf_canto_inf_esq_y and player.canto_inf_dir_y <= self.inf_canto_sup_dir_y:
            return True
        
        return False