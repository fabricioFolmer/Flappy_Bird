import glfw, numpy as np, time
from OpenGL.GL import *
from PIL import Image
from config_manager import ConfigManager

def carregar_textura(path):
    imagem = Image.open(path)
    imagem = imagem.transpose(Image.FLIP_TOP_BOTTOM)
    img_data = np.array(imagem.convert("RGBA"), dtype=np.uint8)

    id_textura = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, id_textura)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, imagem.width, imagem.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    return id_textura

def desenhar_personagem(textura_id, altura):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textura_id)

    largura = 0.1
    altura_sprite = 0.3

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-largura, -0.4 + altura, 0)

    glTexCoord2f(1.0, 0.0)
    glVertex3f(largura, -0.4 + altura, 0)

    glTexCoord2f(1.0, 1.0)
    glVertex3f(largura, -0.4 + altura_sprite + altura, 0)

    glTexCoord2f(0.0, 1.0)
    glVertex3f(-largura, -0.4 + altura_sprite + altura, 0)

    glEnd()

    glDisable(GL_TEXTURE_2D)



def main():
    # Carrega as configurações do jogo
    config = ConfigManager()

    # Inicia o GLFW
    if not glfw.init():
        return

    # Cria uma janela OpenGL
    janela = glfw.create_window(config.get("window_width"), config.get("window_height"), "Personagem com textura", None, None)
    
    # Verifica se a janela foi criada corretamente
    if not janela:
        glfw.terminate()
        return

    # Configurações da janela
    glfw.make_context_current(janela)                   # Faz a janela atual
    glfw.swap_interval(1)                               # Limita a 60 FPS
    glEnable(GL_BLEND)                                  # Define a viewport
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)   # Define a projeção ortográfica

    textura = carregar_textura("textures/character.png")

    # Inicializa variáveis de tempo e física
    tempo_anterior = time.time()
    pulo = False
    velocidade = 0
    altura = 0
    gravidade = -9.8

    # Loop principal do jogo, rodando até que a janela seja fechada
    while not glfw.window_should_close(janela):
        
        
        glClearColor(0.5, 0.7, 1.0, 1) # Cor de fundo: azul claro
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Limpa a tela

        tempo_atual = time.time()
        delta_time = tempo_atual - tempo_anterior
        tempo_anterior = tempo_atual
        delta_time = min(delta_time, 0.05)

        if glfw.get_key(janela, glfw.KEY_SPACE):
            if not pulo:
                pulo = True
                velocidade = 3.5
                altura = 0

        if pulo:
            altura += velocidade * delta_time
            velocidade += gravidade * delta_time
            if altura <= 0:
                pulo = False

        desenhar_personagem(textura, altura)

        glfw.swap_buffers(janela)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()