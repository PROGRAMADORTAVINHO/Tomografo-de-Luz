from PIL import Image
from skimage import util
import os
import numpy as np

# Caminho para a pasta contendo as imagens processadas
caminho_pasta = "C:/Users/Rafa/Documents/Facul/tomografo/imagens_processadas"
caminho_saida_sinogramas = "C:/Users/Rafa/Documents/Facul/tomografo/sinogramas"

# Cria o diretório de saída para sinogramas se não existir
if not os.path.exists(caminho_saida_sinogramas):
    os.makedirs(caminho_saida_sinogramas)

# Lista todos os arquivos na pasta de imagens processadas
arquivos = os.listdir(caminho_pasta)

# Número de imagens por sinograma
imagens_por_sinograma = 200

# Número total de sinogramas a serem gerados
num_sinogramas = 15

# Loop sobre cada grupo de imagens para criar os sinogramas
for i in range(0, len(arquivos), imagens_por_sinograma):
    # Seleciona o grupo de imagens
    grupo_imagens = arquivos[i:i+imagens_por_sinograma]

    # Inicializa uma lista para armazenar as imagens do grupo
    imagens_grupo = []

    # Loop sobre cada arquivo no grupo
    for arquivo in grupo_imagens:
        caminho_imagem = os.path.join(caminho_pasta, arquivo)
        imagem = Image.open(caminho_imagem).convert("L")
        imagem_np = util.img_as_ubyte(np.array(imagem))
        imagens_grupo.append(imagem_np)

    # Concatena as imagens do grupo ao longo do eixo da largura
    imagens_concatenadas = np.concatenate(imagens_grupo, axis=1)

    # Salva a imagem concatenada como sinograma
    caminho_sinograma = os.path.join(caminho_saida_sinogramas, f"sinograma_{i//imagens_por_sinograma + 1}.png")
    Image.fromarray(imagens_concatenadas).save(caminho_sinograma)

    print(f"Sinograma {i//imagens_por_sinograma + 1} foi criado e salvo como {caminho_sinograma}")
