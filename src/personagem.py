import time
from threading import Thread
from src.texturas import carregarTextura
from src.parametros import Parametros

class Personagem:
    def __init__(self):
        
        # Instancia classe de parâmetros do jogo
        cfg = Parametros()

        # Configurações do personagem
        self.largura = cfg.personagem_largura
        self.altura  = cfg.personagem_altura
        self.teto    =  1 - self.altura / 2    # Limite superior da altura do personagem
        self.chao    = -1 + self.altura / 2    # Limite inferior da altura do personagem
        self.vidas   = cfg.personagem_vidas
        self.pontos  = cfg.personagem_pontos
        self.esta_invencivel = False
        self.duracao_invencibilidade = cfg.personagem_duracao_invencibilidade

        # Carrega a imagem com a textura do personagem
        self.textura_id = carregarTextura('texturas/personagem.png')
        self.textura_invencivel_id = carregarTextura('texturas/personagem_invencivel.png')

        self.setPosicao(cfg.personagem_posicao_horizontal, 0)

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

    def registrarColisao(self):
        # Se o personagem não estiver invencível, diminui a vida
        if not self.esta_invencivel and self.vidas > 0:
            # Diminui a vida e ativa a invencibilidade
            self.vidas -= 1
           
            # Se ainda possui vidas, ativa a invencibilidade
            if self.vidas > 0:
                self.ativarInvencibilidade()
    
    def ativarInvencibilidade(self):
        # Ativa a invencibilidade do personagem
        self.esta_invencivel = True
        # Cria uma thread para remover a invencibilidade após o tempo de duração
        # (não bloqueia o jogo enquanto espera)
        t = Thread(target=self.removerInvencibilidade, args=(self.duracao_invencibilidade,)) # TODO Tentar resolver sem threads
        t.start()

    def removerInvencibilidade(self, duracao_invencibilidade):
        # Remove a invencibilidade do personagem após o tempo de duração
        time.sleep(duracao_invencibilidade)
        self.esta_invencivel = False