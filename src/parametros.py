import json, os

# Classe ConfigManager para gerenciar a configuração do jogo
# Se o arquivo de configuração não existir, ele será criado com valores padrão
# Se o arquivo existir, ele será carregado e os valores serão atualizados
class Parametros:
    default_config = {
        "janela_largura": 1280,                     # Pixels
        "janela_altura": 720,                       # Pixels
        "janela_titulo": "Flappy Dragon",           # Título da janela
        
        "valor_gravidade": -9.80665,                # Aceleração da gravidade (m/s²)

        "personagem_posicao_horizontal": -0.45,     # Posição horizontal do personagem (em relação à largura da janela)
        "personagem_largura": 0.15,                 # Largura do personagem (em relação à largura da janela)
        "personagem_altura": 0.225,                 # Altura do personagem (em relação à altura da janela)
        "personagem_velocidade_pulo": 2,            # Velocidade do pulo (em relação à altura da janela por segundo)

        "torre_tempo_1a_geracao": 0.5,              # Tempo para gerar o 1º obstáculo (em segundos)
        "torre_tempo_entre_geracao": 3,             # Tempo entre a geração de obstáculos (em segundos)
        "torre_velocidade_movimento": 0.2,          # Velocidade dos obstáculos (em relação à largura da janela por segundo)
        "torre_altura_do_gap": 0.5,                 # Altura do espaço entre os obstáculos (em relação à altura da janela)
        "torre_largura": 0.23,                      # Largura dos obstáculos (em relação à largura da janela)
        "torre_altura": 1.35                        # Altura máxima dos obstáculos (em relação à altura da janela)
    }

    def __init__(self, filepath="config.json"):
        self.filepath = filepath
        self.config = self.default_config.copy()
        self.load()

    def load(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                try:
                    data = json.load(f)
                    self.config.update(data)
                except json.JSONDecodeError:
                    print("⚠️ Invalid JSON format. Using defaults.")
                    
    def save(self):
        with open(self.filepath, "w") as f:
            json.dump(self.config, f, indent=4)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        self.save()
