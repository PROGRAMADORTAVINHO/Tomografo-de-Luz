import os

import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from matplotlib import cm

#Função para ler as imagens de uma pasta
def ler_imagens(folder_path):
    imagens = []
    for filename in os.listdir(folder_path):
        path = os.path.join(folder_path, filename)
        img = io.imread(path)
        imagens.append(img)
    return imagens

#Pasta contendo as imagens de radon
pasta_imagens = 'F:\\Senac\\4º Semestre\\Fisica Elétrica\\Tomografo\\conjunto 5\\PlanosAxiais'

#Lê as imagens da pasta
imagens = ler_imagens(pasta_imagens)

#Converte as imagens para arrays e plota em um gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i, imagem in enumerate(imagens):
    # Transforma a imagem em um array
    array_imagem = np.array(imagem)

    # Define um limiar para remover os pontos escuros
    limiar = array_imagem.max() * 0.9  # Ajuste o valor do limiar conforme necessário

    # Cria uma máscara para os valores abaixo do limiar
    mascara = array_imagem < limiar

    # Substitui os valores abaixo do limiar por NaN (Not a Number)
    array_imagem = np.where(mascara, np.nan, array_imagem)

    # Pega as dimensões da imagem
    altura, largura = array_imagem.shape

    # Cria uma grade de coordenadas para o gráfico 3D
    x = np.arange(0, largura, 1)
    y = np.arange(0, altura, 1)
    x, y = np.meshgrid(x, y)

    # Usa a colormap para mapear os valores dos pixels para cores
    norm = plt.Normalize(np.nanmin(array_imagem), np.nanmax(array_imagem))
    cores = cm.viridis(norm(array_imagem))

    # Plota a imagem no eixo Z
    ax.plot_surface(x, y, i * np.ones_like(array_imagem), rstride=1, cstride=1, facecolors=cores, shade=False)