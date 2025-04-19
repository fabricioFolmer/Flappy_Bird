from src.texturas import carregarTextura
from src.parametros import Parametros

class Personagem:
    def __init__(self):
        
        # Instancia classe de parâmetros do jogo
        params = Parametros()
        
        # Configurações do personagem
        self.largura = params.get('personagem_largura')
        self.altura  = params.get('personagem_altura')
        self.teto    =  1 - self.altura / 2    # Limite superior da altura do personagem
        self.chao    = -1 + self.altura / 2    # Limite inferior da altura do personagem

        # Carrega a imagem com a textura do personagem
        self.textura_id = carregarTextura('texturas/personagem.png')

        self.setPosicao(params.get('personagem_posicao_horizontal'), 0)

    # Função que atualiza a posição do personagem, recebendo a posição central dele (x e y) e calculando os cantos
    def setPosicao(self, x, y):

        # Não permite que ultrapasse o teto e o chao
        if y > self.teto:
            y = self.teto
        elif y < self.chao:
            y = self.chao

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
        self.posicao = (self.canto_inf_esq_x, self.canto_inf_esq_y, self.canto_inf_dir_x, self.canto_inf_dir_y, self.canto_sup_dir_x, self.canto_sup_dir_y, self.canto_sup_esq_x, self.canto_sup_esq_y)