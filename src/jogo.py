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
        red_pixel_texture_id = carregarTextura('texturas/red_pixel.png') # Usado apenas para debug TODO Remover

        # Instancia classes
        cfg = Parametros()
        player = Personagem()
        window = Window()
        
        # Inicializa variáveis de controle do jogo
        tempo_no_frame_anterior = time.time()                           # Tempo do frame anterior. Usado para calcular o tempo entre frames.
        
        # Variável para controlar o início do jogo. Serve para o jogo não inicar com o personagem caindo.
        game_started = False
        game_over = False
        game_over_freeze = False
        
        # Variável para controlar o pressionamento da tecla de espaço.
        # Serve para evitar que o personagem pule várias vezes seguidas se o usuário segurar a tecla espaço.
        espaco_pressionado_no_frame_anterior = False

        # Variáveis para controles dos obstáculos
        torres = [] # Irá armazenar a posição de todos os obstáculos

        # Loop principal do jogo
        while not glfw.window_should_close(janela):
            
            # Limpa a tela
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
            # Atualiza o tempo
            tempo_atual = time.time()
            delta_time = tempo_atual - tempo_no_frame_anterior
            tempo_no_frame_anterior = tempo_atual
            
            # Verifica se a tecla de espaço foi pressionada ou se foi clicado na tela
            if glfw.get_key(janela, glfw.KEY_SPACE) == glfw.PRESS or glfw.get_mouse_button(janela, glfw.MOUSE_BUTTON_LEFT) == glfw.PRESS:
                
                # Se o jogo não está em andamento, o inicia
                if not game_started:

                    # Se se trata de um recomeço de jogo, reinicia as variáveis
                    if game_over is True:
                        player = Personagem()
                        torres = []
                        game_over = False
                        print('Recomeço de jogo')
                    game_started = True
                    tempo_inicio_jogo = tempo_atual
                    print('Game started')

                if espaco_pressionado_no_frame_anterior is False:
                    espaco_pressionado_no_frame_anterior = True

                    # Registra um pulo
                    velocidade = cfg.valor_velocidade_pulo
            else:
                espaco_pressionado_no_frame_anterior = False
            
            if game_started is True:
                
                # Atualiza a altura do personagem
                player.setPosicao(player.centro_x, player.centro_y + velocidade * delta_time) # Atualiza a altura com base na velocidade e no tempo desde o último frame
                velocidade += cfg.valor_gravidade * delta_time  # Aplica a gravidade à velocidade
                
                # Se já se passou o tempo mínimo para gerar a torre, gera uma nova torre
                if (len(torres) == 0 and tempo_atual - tempo_inicio_jogo >= cfg.torre_tempo_1a_geracao) or (len(torres) > 0 and tempo_atual - tempo_geracao_ultimo_obstaculo >= cfg.torre_tempo_entre_geracao):
                    torres.append(Torre()) # Instancia um novo obstáculo
                    
                    tempo_geracao_ultimo_obstaculo = tempo_atual
                
                # Movimenta as torres para a esquerda
                colisao = False
                for t in torres:
                    t.movimentar(delta_time)
                    
                    # Detecta colisão entre o personagem e os obstáculos
                    if t.colidiu(player) is True:
                        colisao = True

                    # Detecta se o personagem passou completamente pelo obstáculo e registra um ponto se sim
                    if t.gerou_ponto is False and player.canto_sup_esq_x > t.inf_canto_sup_dir_x:
                        player.pontos += 1
                        t.gerou_ponto = True

                # Remove torres que saíram da tela
                for i in torres:
                    if i.inf_canto_sup_dir_x < -1:
                        torres.remove(i)
                        break

                    
            # Desenha o background
            window.desenharBackground()
            
            # Desenha as torres em tela
            for i in torres:
                window.desenharTorre(i)

            # Desenha o personagem na tela
            window.desenharJogador(player)
                
            # Desenha o scoreboard no canto superior esquerdo
            window.desenharScoreboard(vidas = player.vidas, pontos = player.pontos)

            # Se o jogo não inicou nenhuma vez, desenha a tela de boas vindas
            if game_started is False and game_over is False:
                window.desenharInicioDeJogo()

            # Realiza os tratamentos de colisão após desenhar todos os objetos em tela
            if game_started is True:
                if colisao is True:
                    player.registrarColisao()
            
                print(f'Vidas: {player.vidas}, Colidiu: {colisao}, Invencível: {player.esta_invencivel}')  # Usado apenas para debug TODO Remover

            # Se acabaram as vidas
            if player.vidas <= 0:

                # Aguarda 2 segundos antes de reiniciar o jogo, para o jogador ver a tela de Game Over
                if game_over_freeze is True:
                    time.sleep(2)
                    game_over_freeze = False

                # Se o jogo está em andamento, registra o game over. Isso será verdadeiro apenas no 1º frame após o game over
                if game_started is True:
                    game_over_freeze = True # No próximo frame, o jogo irá parar por 2 segundos para o jogador ver a tela de Game Over
                    game_over = True
                    game_started = False
                
                # Desenha a tela de Game Over
                window.desenharFimDeJogo()
                



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
        