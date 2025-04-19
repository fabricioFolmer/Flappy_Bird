## Definição do trabalho
Criar um programa no formato do jogo Flappy Bird utilizando os conceitos de computação gráfica estudados na disciplina

## Lista de Tarefas
|   |    Descrição                                                                         |
|---|--------------------------------------------------------------------------------------|
| ✅ | Inicializar Janela com Plano de Fundo                                               |
| ✅ | Carregar o Personagem com Físicas e Vôo                                             |
| ✅ | Criar Motor de Geração, Movimento e Colisão de Obstáculos                           |
| ✅ | Criar Mecânica de Múltiplas Vidas                                                   |
| ✅ | Criar Scoreboard de Pontos e Vidas e Mostrar em Tela                                |
| ❌ | Ao acabar as vidas, mostrar score board e botão de reiniciar ou sair                |
| ❌ | Criar Powerup aleatório de ganhar vida                                              |
| ❌ | Antes de começar o jogo, mostrar popup instruindo a apertar espaço para iniciar     |
| ❌ | Realizar Ajustes Finos na Documentação e adicionar prints do programa em execução   |
| ❌ | Adicionar Música de Plano de Fundo?                                                 |
| ❌ | Evoluir Detecção de Colisão                                                         |

## Requisitos do programa
- Deve ser feito na linguagem Python;
- Será permitido utilizar somente as seguintes bibliotecas:
    - PyOpenGL_accelerate;
    - glfw;
    - Pillow (PIL);
    - time;
    - numpy;
    - random.

## Formato do trabalho
- O trabalho poderá ser feito em grupos de até 5 pessoas
- A apresentação de cada trabalho será feita para o professor
- Cada grupo terá o tempo máximo de 10 minutos com tolerância de 5 minutos para apresentar

## Critérios de avaliação
| Pontuação | Item   |
|-----------|--------|
| 1 Ponto   | Fazer o personagem voar apertando a tecla ESPAÇO |
| 1 Ponto   | Fazer os obstáculos e personagem se movimentarem |
| 1 Ponto   | Realizar o tratamento de colisão |
| 1 Ponto   | Contador de quantos obstáculos já passou |
| 1 Ponto   | Exibir um contador de vidas, o jogo só finaliza quando termina o número de vidas |
| 1 Ponto   | Criar objetos que aparecem aleatoriamente no jogo, pode ser vidas, alternador de velocidade, etc |
| 1 Ponto   | A entrega do trabalho deverá ser feita enviando os arquivos do projeto no ambiente virtual e compartilhando um link do github que conste todo o código fonte, uma explicação do projeto e algumas telas do jogo |
| 3 Ponto   | Apresentação do trabalho |

### Apresentação do trabalho
- Na apresentação todos devem falar, será feito perguntas específicas para cada integrante do grupo. Será descontado pontos da nota do trabalho caso algum integrante não responda adequadamente às perguntas.
- Devem ser utilizados os comandos vistos em aula, podem ser utilizados comandos adicionais. Atenção! Se a estrutura do programa for diferente do que foi visto em aula, será descontado pontos


## Dicas
- Podem personalizar os personagens e obstáculos, usem a criatividade!;
- Tanto o personagem quanto os obstáculos podem ser representados por qualquer primitiva geométrica;
- Fiquem livre para criar conceitos de vida, condição para terminar o jogo, pontuação, ranking, etc.;
- Pode ser feito tanto no ambiente 2D quanto no 3D;
- Utilizem a variável de tempo para controlar os movimentos das primitivas;
- Fiquem livres para criar múltiplas classes ou arquivos para o projeto;
- Utilizem vetores para armazenar as posições;
- Definam variáveis públicas para determinar o tamanho dos sprites, range de colisão, velocidade, etc..


## Requerimentos para Execução
- Python 3.10;
- Instação das seguintes bibliotecas: `pip install numpy glfw Pillow PyOpenGL PyOpenGL_accelerate`.