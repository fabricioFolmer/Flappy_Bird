from src.window import Window
from src.main_game import Game

if __name__ == "__main__":
    
    # Inicia a janela do jogo
    janela = Window.initializeWindow()

    # Loop principal do jogo, rodando até que a janela seja fechada
    Game.run(janela)