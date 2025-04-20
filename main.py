import glfw, time, random, threading
from OpenGL.GL import *
from src.parametros import Parametros
from src.janela import Window
from src.personagem import Personagem
from src.torre import Torre
from src.power_up import PowerUp
from src.sound_mixer import iniciarSoundtrack


if __name__ == "__main__":

    # Inicia a janela do jogo
    janela = Window.iniciarJanela()

    # Inicia a soundtrack do jogo em uma Thread exclusiva
    threading.Thread(target=iniciarSoundtrack, daemon=True).start()
    
    # Instancia classes
    cfg = Parametros()
    player = Personagem()
    window = Window()

    # Inicializa variáveis de controle do jogo
    tempo_no_frame_anterior = time.time()                           # Tempo do frame anterior. Usado para calcular o tempo entre frames.

    # Variáveis para controlar o estado do jogo.
    game_started = False
    game_over = False
    game_over_freeze = False

    # Variável para controlar o tempo restante de invencibilidade do personagem.
    countdown_invencibilidade = None

    # Variável para controlar o pressionamento da tecla de espaço.
    # Serve para evitar que o personagem pule várias vezes seguidas se o usuário segurar a tecla espaço.
    espaco_pressionado_no_frame_anterior = False

    # Variáveis para controles dos objetos
    torres = [] # Irá armazenar a posição de todos os obstáculos
    power_ups = [] # Irá armazenar a posição de todos os power ups

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
                tempo_prox_pwr_up = random.uniform(0.1, cfg.power_up_tempo_entre_geracao) # Tempo para gerar o próximo power up
                tempo_cooldown_pwr_up = cfg.power_up_tempo_entre_geracao # Tempo de cooldown do power up
                print('Game started')

            # Se a tecla de espaço foi pressionada no frame atual, registra um pulo no personagem
            if espaco_pressionado_no_frame_anterior is False:
                espaco_pressionado_no_frame_anterior = True
                velocidade = cfg.valor_velocidade_pulo
        
        else:
            espaco_pressionado_no_frame_anterior = False
        
        if game_started is True:
            
            # Atualiza a altura do personagem
            player.setPosicao(player.centro_x, player.centro_y + velocidade * delta_time) # Atualiza a altura com base na velocidade e no tempo desde o último frame
            velocidade += cfg.valor_gravidade * delta_time  # Aplica a gravidade à velocidade
            
            # Reduz o tempo do último frame nas variáveis de contagem regressiva
            tempo_prox_pwr_up -= delta_time
            tempo_cooldown_pwr_up = max(tempo_cooldown_pwr_up - delta_time, 0)
            if countdown_invencibilidade is not None:
                countdown_invencibilidade -= delta_time

            # Se o tempo de invencibilidade do personagem estiver zerado, desativa a invencibilidade
            if countdown_invencibilidade is not None and countdown_invencibilidade <= 0:
                player.esta_invencivel = False
                countdown_invencibilidade = None

            # Se já se passou o tempo mínimo para gerar a torre, gera uma nova torre
            if (len(torres) == 0 and tempo_atual - tempo_inicio_jogo >= cfg.torre_tempo_1a_geracao) or (len(torres) > 0 and tempo_atual - tempo_geracao_ultimo_obstaculo >= cfg.torre_tempo_entre_geracao):
                torres.append(Torre()) # Instancia um novo obstáculo
                tempo_geracao_ultimo_obstaculo = tempo_atual
            
            # Movimenta as torres para a esquerda
            colisao = False
            torre_mais_a_direita = 0 # Guarda a coordenada X da torre mais a direita, para ser usada na verificação de geração de power ups
            for t in torres:
                t.movimentar(delta_time)
                
                # Detecta colisão entre o personagem e os obstáculos
                if t.colidiu_jogador_torre(player) is True:
                    colisao = True

                # Detecta se o personagem passou completamente pelo obstáculo e registra um ponto se sim
                if t.gerou_ponto is False and player.canto_sup_esq_x > t.inf_canto_sup_dir_x:
                    player.pontos += 1
                    t.gerou_ponto = True

                # Guarda informação da coordenada X da torre mais a direita, para ser usada na verificação de geração de power ups
                if t.inf_canto_sup_dir_x > torre_mais_a_direita:
                    torre_mais_a_direita = t.inf_canto_sup_dir_x

            # Remove torres que saíram da tela
            for t in torres:
                if t.inf_canto_sup_dir_x < -1:
                    torres.remove(t)
                    break

            # Se já se passou o tempo mínimo para gerar o power up, gera um novo power up
            if tempo_prox_pwr_up <= 0:
                # Se existe uma torre após o fim da tela, gera o Power Up após ela
                if torre_mais_a_direita > 1:
                    power_ups.append(PowerUp(offset_x_geracao = cfg.torre_largura + cfg.power_up_largura / 2))
                else:
                    power_ups.append(PowerUp())

                # Adicona o tempo de cooldown mais 1 segundo no tempo de geração do próximo power up para não gerar power ups em sequência
                tempo_prox_pwr_up = tempo_cooldown_pwr_up + 1

            # Se o cooldown do power up estiver zerado, gera um novo power up e reinicia o tempo de cooldown
            if tempo_cooldown_pwr_up <= 0:

                tempo_prox_pwr_up = random.uniform(0.1, cfg.power_up_tempo_entre_geracao)
                tempo_cooldown_pwr_up = cfg.power_up_tempo_entre_geracao

            # Movimenta os power ups para a esquerda
            for p in power_ups:
                p.movimentar(delta_time)

            # Detecta colisão entre o personagem e os power ups. Se sim, adiciona vida e remove o power up da lista
            for p in power_ups:
                if p.colidiu_jogador_powerup(player) is True:
                    player.vidas += 1
                    power_ups.remove(p)
                    break

            # Remove powerups que saíram da tela
            for p in power_ups:
                if p.canto_inf_dir_x < -1:
                    power_ups.remove(p)
                    break

        # Desenha o background
        window.desenharBackground()
        
        # Desenha as torres em tela
        for i in torres:
            window.desenharTorre(i)

        # Desenha os power ups em tela
        for i in power_ups:
            window.desenharPowerUp(i)

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
                # Se o personagem não estiver invencível, diminui a vida
                if not player.esta_invencivel and player.vidas > 0:
                    # Diminui a vida e ativa a invencibilidade
                    player.vidas -= 1
                
                    # Se ainda possui vidas, ativa a invencibilidade
                    if player.vidas > 0:
                        player.esta_invencivel = True
                        countdown_invencibilidade = cfg.personagem_duracao_invencibilidade # Inicia o countdown da invencibilidade

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
            
        # Atualiza a janela
        glfw.swap_buffers(janela)   # Troca os buffers da janela
        glfw.poll_events()          # Processa eventos da janela

    # Libera os recursos ao fechar o jogo
    glfw.terminate()
