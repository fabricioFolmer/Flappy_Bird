import glfw, numpy as np
from OpenGL.GL import *
from PIL import Image
from src.config_manager import ConfigManager
from src.textures import LoadTexture

class Window:
    def initializeWindow():
        
        # Carrega as configurações do jogo
        config = ConfigManager()
        
        # Inicia o GLFW
        if not glfw.init():
            return

        # Cria uma janela OpenGL
        janela = glfw.create_window(config.get("window_width"), config.get("window_height"), config.get("window_title"), None, None)

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

    def drawTexture(texture_id, bottomLeftHorizontalPosition, bottomLeftVerticalPosition, bottomRightHorizontalPosition, bottomRightVerticalPosition, topRightHorizontalPosition, topRightVerticalPosition, topLeftHorizontalPosition, topLeftVerticalPosition):


        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, texture_id)


        glBegin(GL_QUADS)

        # Canto inferior esquerdo
        glTexCoord2f(0.0, 0.0)
        glVertex3f(bottomLeftHorizontalPosition, bottomLeftVerticalPosition, 0)

        # Canto inferior direito
        glTexCoord2f(1.0, 0.0)
        glVertex3f(bottomRightHorizontalPosition, bottomRightVerticalPosition, 0)

        # Canto superior direito
        glTexCoord2f(1.0, 1.0)
        glVertex3f(topRightHorizontalPosition, topRightVerticalPosition, 0)

        # Canto superior esquerdo
        glTexCoord2f(0.0, 1.0)
        glVertex3f(topLeftHorizontalPosition, topLeftVerticalPosition, 0)

        glEnd()
        glDisable(GL_TEXTURE_2D)
