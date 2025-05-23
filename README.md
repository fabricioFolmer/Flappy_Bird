## Descrição
Programa no formato do jogo Flappy Bird utilizando a API do OpenGL para Python para implementar.

## Disclaimer
- A biblioteca `Pygame` foi utilizada exclusivamente para reprodução de músicas durante a execução do jogo, uma funcionalidade que não é oferecida nativamente pelo Python;
- As faixas de áudio presentes na pasta `soundtrack` pertencem à trilha sonora original do jogo Cuphead e estão sujeitas a direitos autorais;
- O plano de fundo do jogo e os obstáculos foram retirados de um dos níveis de Cuphead;
- Com exceção dos elementos visuais mencionados acima, todas as demais artes foram geradas com o auxílio de Inteligência Artificial Generativa.

## Lista de Tarefas
|   |    Descrição                                                                         |
|---|--------------------------------------------------------------------------------------|
| ✅ | Inicializar Janela com Plano de Fundo                                               |
| ✅ | Carregar o Personagem com Físicas e Vôo                                             |
| ✅ | Criar Motor de Geração, Movimento e Colisão de Obstáculos                           |
| ✅ | Criar Mecânica de Múltiplas Vidas                                                   |
| ✅ | Criar Scoreboard de Pontos e Vidas e Mostrar em Tela                                |
| ✅ | Ao acabar as vidas, mostrar scoreboard e botão de reiniciar ou sair                 |
| ✅ | Criar Powerup aleatório de ganhar vida                                              |
| ✅ | Antes de começar o jogo, mostrar popup instruindo a apertar espaço para iniciar     |
| ✅ | Revisar Código e Documentação e adicionar prints do programa em execução no Git     |
| ✅ | Adicionar Trilha Sonora                                                             |

## Requerimentos para Execução
- Python 3.10;
- Instação das seguintes bibliotecas: `pip install numpy glfw Pillow PyOpenGL PyOpenGL_accelerate pygame`.

## Screenshots do Jogo em Execução

### 1. Tela Inicial
![Game Screenshot](assets/1_Tela_Inicial.png)

### 2. Jogo em Andamento
![Game Screenshot](assets/2_Jogo_em_Andamento.png)

### 3. Fim de Jogo
![Game Screenshot](assets/3_Fim_de_Jogo.png)