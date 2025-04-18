import numpy as np
from OpenGL.GL import *
from PIL import Image


def LoadTexture(path):
    imagem = Image.open(path)
    imagem = imagem.transpose(Image.FLIP_TOP_BOTTOM)
    img_data = np.array(imagem.convert("RGBA"), dtype=np.uint8)

    id_textura = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, id_textura)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, imagem.width, imagem.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    return id_textura
