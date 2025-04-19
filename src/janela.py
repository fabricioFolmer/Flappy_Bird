import glfw, numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *  # Import GLUT for glutBitmapCharacter
from OpenGL.GLUT.fonts import GLUT_BITMAP_HELVETICA_12, GLUT_BITMAP_HELVETICA_18, GLUT_BITMAP_TIMES_ROMAN_10, GLUT_BITMAP_TIMES_ROMAN_24
from src.parametros import Parametros
from src.texturas import carregarTextura
from PIL import Image  # Biblioteca para manipular imagens

class Window:
    def __init__(self):
        
        # Salva id das texturas nessa classe, quando instanciada
        self.id_textura_background = carregarTextura('texturas/background.jpg')
        self.id_textura_scoreboard_background = carregarTextura('texturas/scoreboard_background.jpg')
        self.id_textura_vida = carregarTextura('texturas/vida.png')
        self.id_textura_inicio_de_jogo = carregarTextura('texturas/inicio_de_jogo.png')
        self.id_textura_fim_de_jogo = carregarTextura('texturas/fim_de_jogo.png')


    def iniciarJanela():
        
        # Carrega as configurações do jogo
        cfg = Parametros()
        
        # Inicia o GLFW
        if not glfw.init():
            return

        # Cria uma janela OpenGL
        janela = glfw.create_window(cfg.janela_largura, cfg.janela_altura, cfg.janela_titulo, None, None)

        # Verifica se a janela foi criada corretamente
        if not janela:
            glfw.terminate()
            return
        
        # Posiciona a janela no centro da tela
        monitor_size = glfw.get_video_mode(glfw.get_primary_monitor()).size
        window_size = glfw.get_window_size(janela)
        x_pos = (monitor_size.width - window_size[0]) // 2
        y_pos = (monitor_size.height - window_size[1]) // 2
        glfw.set_window_pos(janela, x_pos, y_pos)
        
        # Configurações da janela
        glfw.make_context_current(janela)                   # Faz a janela atual
        glfw.swap_interval(1)                               # Limita a 60 FPS
        glEnable(GL_BLEND)                                  # Define a viewport
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)   # Define a projeção ortográfica

        return janela

    # Recebe a textura e as coordenadas dos vértices de um quadrado e o desenha na tela
    def desenharTextura(self, id_textura, canto_inf_esq_x, canto_inf_esq_y, canto_inf_dir_x, canto_inf_dir_y, canto_sup_dir_x, canto_sup_dir_y, canto_sup_esq_x, canto_sup_esq_y):

        glEnable(GL_TEXTURE_2D)                     # Habilita o uso de texturas
        glBindTexture(GL_TEXTURE_2D, id_textura)    # Associa a textura à ID
        glBegin(GL_QUADS)                           # Inicia o desenho de um quadrado

        # Canto inferior esquerdo
        glTexCoord2f(0.0, 0.0)
        glVertex3f(canto_inf_esq_x, canto_inf_esq_y, 0)

        # Canto inferior direito
        glTexCoord2f(1.0, 0.0)
        glVertex3f(canto_inf_dir_x, canto_inf_dir_y, 0)

        # Canto superior direito
        glTexCoord2f(1.0, 1.0)
        glVertex3f(canto_sup_dir_x, canto_sup_dir_y, 0)

        # Canto superior esquerdo
        glTexCoord2f(0.0, 1.0)
        glVertex3f(canto_sup_esq_x, canto_sup_esq_y, 0)

        glEnd()                                     # Finaliza o desenho do quadrado
        glDisable(GL_TEXTURE_2D)                    # Desabilita o uso de texturas

    # Renderiza o jogador na tela
    def desenharJogador(self, player):
        
        # Se estiver invencível, desenha o personagem com uma textura diferente
        if player.esta_invencivel:
            self.desenharTextura(player.textura_invencivel_id, player.canto_inf_esq_x, player.canto_inf_esq_y, player.canto_inf_dir_x, player.canto_inf_dir_y, player.canto_sup_dir_x, player.canto_sup_dir_y, player.canto_sup_esq_x, player.canto_sup_esq_y)
        else:
            self.desenharTextura(player.textura_id, player.canto_inf_esq_x, player.canto_inf_esq_y, player.canto_inf_dir_x, player.canto_inf_dir_y, player.canto_sup_dir_x, player.canto_sup_dir_y, player.canto_sup_esq_x, player.canto_sup_esq_y)

    # Desenha a torre na tela
    def desenharTorre(self, torre):

        # Desenha a torre superior
        self.desenharTextura(torre.textura_superior_id, torre.sup_canto_inf_esq_x, torre.sup_canto_inf_esq_y, torre.sup_canto_inf_dir_x, torre.sup_canto_inf_dir_y, torre.sup_canto_sup_dir_x, torre.sup_canto_sup_dir_y, torre.sup_canto_sup_esq_x, torre.sup_canto_sup_esq_y)
        
        # Desenha a torre inferior
        self.desenharTextura(torre.textura_inferior_id, torre.inf_canto_inf_esq_x, torre.inf_canto_inf_esq_y, torre.inf_canto_inf_dir_x, torre.inf_canto_inf_dir_y, torre.inf_canto_sup_dir_x, torre.inf_canto_sup_dir_y, torre.inf_canto_sup_esq_x, torre.inf_canto_sup_esq_y)

    # Desenha o background da tela
    def desenharBackground(self):
        self.desenharTextura(self.id_textura_background, -1, -1, 1, -1, 1, 1, -1, 1)

    # Desenha o scoreboard do jogo
    def desenharScoreboard(self, vidas, pontos):
        self.desenharTextura(self.id_textura_scoreboard_background, -0.98, 0.76, -0.58, 0.76, -0.58, 0.965, -0.98, 0.965)

        # Desenha as vidas (textura é quadrada, então a largura e altura são iguais)
        for i in range(vidas):
            # Parâmetros do posicionamento das vidas
            canto_x = -0.966         # Limite esquerdo da textura das vidas
            canto_y = 0.95           # Limite superior da textura das vidas
            largura_vida = 0.04
            espacamento_entre_vidas = 0.01
            altura_vida = largura_vida * (1280/ 720)    # Altura é igual a largura pois é um quadrado, mas abaixo é feito um ajuste em razão da proporção de tela não ser 1:1 # TODO Ajustar para ser dinâmico à resolução da tela
            self.desenharTextura(self.id_textura_vida, canto_x + (largura_vida + espacamento_entre_vidas) * i, canto_y - altura_vida, canto_x + largura_vida + (largura_vida + espacamento_entre_vidas) * i, canto_y - altura_vida, canto_x + largura_vida + (largura_vida + espacamento_entre_vidas) * i, canto_y, canto_x + (largura_vida + espacamento_entre_vidas) * i, canto_y)

        # Desenha a palavra "Pontuação:"
        self.desenharTexto(-0.95, 0.8, "Pontuação:")

        # Desenha a pontuação atual
        self.desenharTexto(-0.75, 0.8, str(pontos))

    # Desenha o texto na tela. Cor padrão é branco. Fonte é Times Roman 24
    def desenharTexto(self, x, y, texto, cor_rgb = [1, 1, 1]):
        glColor3f(cor_rgb[0], cor_rgb[1], cor_rgb[2])
        glColor3f(1.0, 1.0, 1.0)

        # Define a posição do texto
        glRasterPos2f(x, y)

        # Desenha o texto
        glutInit()
        for char in texto:
            # Desenha cada caractere usando a fonte GLUT_BITMAP_HELVETICA_12
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))
            # glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

    def desenharInicioDeJogo(self):
        # Desenha a tela de fim de jogo no centro da tela
        # Largura em relação a janela = 0.5
        # Altura em relação a janela = 0.555
        self.desenharTextura(self.id_textura_inicio_de_jogo, -0.25, -0.2775, 0.25, -0.2775, 0.25, 0.2775, -0.25, 0.2775)
        
    def desenharFimDeJogo(self):
        # Desenha a tela de fim de jogo no centro da tela
        # Largura em relação a janela = 0.5
        # Altura em relação a janela = 0.555
        self.desenharTextura(self.id_textura_fim_de_jogo, -0.25, -0.2775, 0.25, -0.2775, 0.25, 0.2775, -0.25, 0.2775)
