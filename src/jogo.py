import glfw, time
from OpenGL.GL import *
from src.parametros import Parametros
from src.janela import Window
from src.texturas import carregarTextura
from src.personagem import Personagem
from src.torre import Torre


class Jogo:
    def run():
        
        # Inicia a janela do jogo
        janela = Window.iniciarJanela()

        # Carrega texturas
        textura_background = carregarTextura('texturas/background.jpg')
        red_pixel_texture_id = carregarTextura('texturas/red_pixel.png')

        # Instancia classes
        config = Parametros()
        player = Personagem()
        window = Window()
        
        # Inicializa variáveis de controle do jogo
        tempo_no_frame_anterior = time.time()                           # Tempo do frame anterior. Usado para calcular o tempo entre frames.
        
        # Variável para controlar o início do jogo. Serve para o jogo não inicar com o personagem caindo.
        game_started = False
        
        # Variável para controlar o pressionamento da tecla de espaço.
        # Serve para evitar que o personagem pule várias vezes seguidas se o usuário segurar a tecla espaço.
        espaco_pressionado_no_frame_anterior = False

        # Variáveis para controles dos obstáculos
        torres = [] # Irá armazenar a posição de todos os obstáculos
        tempo_geracao_1o_obstaculo = config.get('torre_tempo_1a_geracao') # Tempo para gerar o 1º obstáculo
        tempo_geracao_obstaculos = config.get('torre_tempo_entre_geracao') # Tempo de geração dos obstáculos

        # Loop principal do jogo
        while not glfw.window_should_close(janela):
            
            # Limpa a tela
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
            # Desenha o background
            window.desenharTextura(textura_background, -1, -1, 1, -1, 1, 1, -1, 1)
            
            # Atualiza o tempo
            tempo_atual = time.time()
            delta_time = tempo_atual - tempo_no_frame_anterior
            tempo_no_frame_anterior = tempo_atual
            
            # Verifica se a tecla de espaço foi pressionada ou se foi clicado na tela
            if glfw.get_key(janela, glfw.KEY_SPACE) == glfw.PRESS or glfw.get_mouse_button(janela, glfw.MOUSE_BUTTON_LEFT) == glfw.PRESS:
                
                # Se o jogo ainda não iniciou, o inicia
                if not game_started:
                    game_started = True
                    tempo_inicio_jogo = tempo_atual
                    print('Game started')

                if espaco_pressionado_no_frame_anterior is False:
                    espaco_pressionado_no_frame_anterior = True

                    # Registra um pulo
                    velocidade = config.get('personagem_velocidade_pulo')
            else:
                espaco_pressionado_no_frame_anterior = False
            
            if game_started is True:
                
                # Atualiza a altura do personagem
                player.setPosicao(player.centro_x, player.centro_y + velocidade * delta_time) # Atualiza a altura com base na velocidade e no tempo desde o último frame
                velocidade += config.get('valor_gravidade') * delta_time  # Aplica a gravidade à velocidade
                
                # Se já se passou o tempo mínimo para gerar a torre, o faz
                if (len(torres) == 0 and tempo_atual - tempo_inicio_jogo >= tempo_geracao_1o_obstaculo) or (len(torres) > 0 and tempo_atual - tempo_geracao_ultimo_obstaculo >= tempo_geracao_obstaculos):
                    torres.append(Torre()) # Instancia um novo obstáculo
                    
                    # torres.append([1 + largura_obstaculo / 2, random.uniform(-altura_maxima_centro_gap, altura_maxima_centro_gap)]) # Adiciona obstáculo com posição vertical aleatória, um pouco além do canto direito da tela
                    tempo_geracao_ultimo_obstaculo = tempo_atual
                
                # Movimenta as torres para a esquerda
                for t in torres:
                    t.movimentar(delta_time)
                    # Se o obstáculo sair da tela, remove-o da lista
                    if t.inf_canto_sup_dir_x < -1:
                        print('Removendo obstáculo')
                        torres.remove(t)
                        break
                    
            # Desenha o personagem na tela
            window.desenharJogador(player)

            # Desenha as torres em tela
            for i in torres:
                window.desenharTorre(i)
                

            # Detecta colisão entre o personagem e os obstáculos
            colisao  = False
            for i in torres:
                if i.colidiu(player) is True:
                    print('Colidiu')
                    colisao  = True
                    break
            if colisao is True:
                print('Colidiu')
            else:
                print('OK')

#
            # Desenho de um pixel vermelho para debug
#            h, v, offset = 0, 0.6, 0.01
#            Window.drawTexture(red_pixel_texture_id, h - offset, v - offset, h + offset, v - offset, h + offset, v + offset, h - offset, v + offset)
            
            # Printa a posição atual do personagem
#            if game_started is True:
#                print(f'Altura: {posicao_vertical}, Velocidade: {velocidade}')

            # Atualiza a janela
            glfw.swap_buffers(janela)   # Troca os buffers da janela
            glfw.poll_events()          # Processa eventos da janela
        
            
        # Libera os recursos ao fechar o jogo
        glfw.terminate()
        