import json, os

# Classe ConfigManager para gerenciar a configuração do jogo
# Se o arquivo de configuração não existir, ele será criado com valores padrão
# Se o arquivo existir, ele será carregado e os valores serão atualizados
class ConfigManager:
    default_config = {
        "window_width": 1280,
        "window_height": 720,
        "window_title": "Flappy Dragon"
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
