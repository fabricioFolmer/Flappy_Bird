import glfw, numpy as np, time
from OpenGL.GL import *
from PIL import Image
from src.config_manager import ConfigManager
from src.window import Window
from src.textures import LoadTexture


class Game:
    def run(janela):
        # Carrega texturas
        character_texture_id = LoadTexture("textures/character.png")
        background_texture_id = LoadTexture('textures/background.jpg')

        # Inicializa variáveis de tempo e física
        GRAVITY = -9.80665
        ALTURA_MAXIMA = 1.0
        ALTURA_MINIMA = -0.5
        POSICAO_HORIZONTAL = -0.45
        velocidade = 0
        altura = 0
        tempo_no_frame_anterior = time.time()
        largura = 0.1
        altura_sprite = 0.3
        
        # Variável para controlar o início do jogo. Serve para o jogo não inicar com o personagem caindo.
        game_started = False
        
        # Variável para controlar o pressionamento da tecla de espaço.
        # Serve para evitar que o personagem pule várias vezes seguidas se o usuário segurar a tecla espaço.
        espaco_pressionado_no_frame_anterior = False

        # Loop principal do jogo
        while not glfw.window_should_close(janela):
            
            # Limpa a tela
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
            # Desenha o background
            Window.drawTexture(background_texture_id, -1, -1, 1, -1, 1, 1, -1, 1)

            # Atualiza o tempo
            tempo_atual = time.time()
            delta_time = tempo_atual - tempo_no_frame_anterior
            tempo_no_frame_anterior = tempo_atual
            delta_time = min(delta_time, 0.05) # Limita o delta_time em no máximo 50ms para evitar problemas de física
            

            # Verifica se a tecla de espaço foi pressionada apenas uma vez
            if glfw.get_key(janela, glfw.KEY_SPACE):
                
                # Se o jogo ainda não iniciou, o inicia
                if not game_started:
                    game_started = True
                    print('Game started')

                else:
                    if espaco_pressionado_no_frame_anterior is False:
                        espaco_pressionado_no_frame_anterior = True
                        print('Tecla pressionada')

                        # Registra um pulo
                        velocidade = 3.5
            else:
                espaco_pressionado_no_frame_anterior = False
            
            if game_started is True:
                
                # Atualiza a altura do personagem
                altura += velocidade * delta_time   # Atualiza a altura com base na velocidade e no tempo desde o último frame
                velocidade += GRAVITY * delta_time  # Aplica a gravidade à velocidade
                
                # Limita a altura máxima do personagem
                if altura >= ALTURA_MAXIMA:
                    altura = ALTURA_MAXIMA

                # Limita a altura mínima do personagem
                if altura <= ALTURA_MINIMA:
                    altura, velocidade = ALTURA_MINIMA, 0

            # Desenha o personagem na tela
            Window.drawTexture(
                character_texture_id, 
                -largura + POSICAO_HORIZONTAL,  -0.4 + altura,                  # Canto inferior esquerdo
                 largura + POSICAO_HORIZONTAL,  -0.4 + altura,                  # Canto inferior direito
                 largura + POSICAO_HORIZONTAL,  -0.4 + altura + altura_sprite,  # Canto superior direito
                -largura + POSICAO_HORIZONTAL,  -0.4 + altura + altura_sprite   # Canto superior esquerdo
            )

            # Atualiza a janela
            glfw.swap_buffers(janela)   # Troca os buffers da janela
            glfw.poll_events()          # Processa eventos da janela

            # Printa a posição atual do personagem
            print(f'Altura: {altura}, Velocidade: {velocidade}')

            
        # Libera os recursos ao fechar o jogo
        glfw.terminate()
        