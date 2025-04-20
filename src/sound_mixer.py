import random
import time
import os

def iniciarSoundtrack():
    """
    Inicia a trilha sonora do jogo. Toca músicas aleatórias da pasta "soundtrack".
    """

    try:
        
        # Popula a lista de músicas com os arquivos .mp3 da pasta soundtrack
        track_list = [ os.path.join("soundtrack", file) for file in os.listdir("soundtrack") if file.endswith(".mp3") ]

        # Verifica se a lista de músicas está vazia
        if not track_list:
            raise FileNotFoundError("Nenhum arquivo .mp3 encontrado na pasta 'soundtrack'.")

        from pygame import mixer

        # Inicializa o mixer do pygame
        mixer.init()

        # Configura o volume
        mixer.music.set_volume(0.1)

        # Indefinidamente toca músicas aleatórias da lista de músicas
        while True:
            track = random.choice(track_list)
            mixer.music.load(track)
            mixer.music.play()
            
            # Aguarda o término da música antes de tocar a próxima
            while mixer.music.get_busy():
                time.sleep(1)

    # Ignora erros de arquivo, caso a pasta "soundtrack" não exista ou esteja vazia
    except FileNotFoundError as e:
        pass
    
    # Ignora erros de importação do módulo mixer, caso o pygame não esteja instalado
    except ImportError:
        pass
