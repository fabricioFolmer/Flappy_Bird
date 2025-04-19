import glfw
from OpenGL.GL import *
from src.parametros import Parametros

class Window:
    def iniciarJanela():
        
        # Carrega as configurações do jogo
        params = Parametros()
        
        # Inicia o GLFW
        if not glfw.init():
            return

        # Cria uma janela OpenGL
        janela = glfw.create_window(params.get("janela_largura"), params.get("janela_altura"), params.get("janela_titulo"), None, None)

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

    # Renderiza o jogador na tela
    def desenharJogador(self, player):
        self.desenharTextura(player.textura_id, player.canto_inf_esq_x, player.canto_inf_esq_y, player.canto_inf_dir_x, player.canto_inf_dir_y, player.canto_sup_dir_x, player.canto_sup_dir_y, player.canto_sup_esq_x, player.canto_sup_esq_y)

    # Desenha a torre na tela
    def desenharTorre(self, torre):

        # Desenha a torre superior
        self.desenharTextura(torre.textura_superior_id, torre.sup_canto_inf_esq_x, torre.sup_canto_inf_esq_y, torre.sup_canto_inf_dir_x, torre.sup_canto_inf_dir_y, torre.sup_canto_sup_dir_x, torre.sup_canto_sup_dir_y, torre.sup_canto_sup_esq_x, torre.sup_canto_sup_esq_y)
        
        # Desenha a torre inferior
        self.desenharTextura(torre.textura_inferior_id, torre.inf_canto_inf_esq_x, torre.inf_canto_inf_esq_y, torre.inf_canto_inf_dir_x, torre.inf_canto_inf_dir_y, torre.inf_canto_sup_dir_x, torre.inf_canto_sup_dir_y, torre.inf_canto_sup_esq_x, torre.inf_canto_sup_esq_y)

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
