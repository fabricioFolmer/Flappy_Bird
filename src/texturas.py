import numpy as np
from OpenGL.GL import *
from PIL import Image

# Recebe o caminho da imagem e retorna o id no OpenGL da textura criada
def carregarTextura(path):

    # Abre a imagem e a converte para o formato RGBA
    imagem = Image.open(path)
    imagem = imagem.transpose(Image.FLIP_TOP_BOTTOM)                # Inverte a imagem verticalmente pois o OpenGL considera a origem no canto inferior esquerdo
    img_data = np.array(imagem.convert("RGBA"), dtype=np.uint8)     # Converte a imagem para um array numpy de 8 bits sem sinal (uint8)

    # Cria a textura no OpenGL
    # Gera um id para a textura
    id_textura = glGenTextures(1)

    # Vincula a textura criada ao id_textura
    glBindTexture(GL_TEXTURE_2D, id_textura)

    # Define a textura
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, imagem.width, imagem.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    
    return id_textura
