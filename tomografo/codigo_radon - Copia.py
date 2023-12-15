import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from skimage import util, transform

# Caminho para a pasta contendo os sinogramas
caminho_sinogramas = "C:/Users/Rafa/Documents/Facul/tomografo/sinogramas"

# Cria o diretório de saída para imagens reconstruídas se não existir
caminho_saida_reconstrucao = "C:/Users/Rafa/Documents/Facul/tomografo/transformadas"
if not os.path.exists(caminho_saida_reconstrucao):
    os.makedirs(caminho_saida_reconstrucao)

# Lista todos os arquivos na pasta de sinogramas
arquivos_sinogramas = os.listdir(caminho_sinogramas)

# Ordena os arquivos para garantir a ordem correta
arquivos_sinogramas.sort()

# Loop sobre cada sinograma para realizar a reconstrução
for i, sinograma in enumerate(arquivos_sinogramas):
    # Carrega o sinograma
    caminho_sinograma = os.path.join(caminho_sinogramas, sinograma)
    sinograma_imagem = Image.open(caminho_sinograma).convert("L")
    sinograma_np = util.img_as_ubyte(np.array(sinograma_imagem))

    # Aplica a transformada inversa de Radon para reconstruir a imagem
    imagem_reconstruida = transform.iradon(sinograma_np, theta=None, circle=True)

    # Normaliza os valores da imagem reconstruída para o intervalo [0, 255]
    imagem_reconstruida = (imagem_reconstruida - np.min(imagem_reconstruida)) / \
                           (np.max(imagem_reconstruida) - np.min(imagem_reconstruida)) * 255

    # Inverte as intensidades para que as partes mais densas sejam brancas
    imagem_reconstruida = 75 - imagem_reconstruida.astype(np.uint8)

    # Salva a imagem reconstruída
    caminho_reconstrucao = os.path.join(caminho_saida_reconstrucao, f"reconstrucao_{i + 1}.png")
    Image.fromarray(imagem_reconstruida).save(caminho_reconstrucao)

    # Plotagem da imagem transformada e do sinograma
    fig, ax = plt.subplots(1, 2, figsize=(12, 4))

    ax[0].imshow(imagem_reconstruida, cmap='gray')
    ax[0].set_title(f'Imagem Transformada {i + 1}')

    ax[1].imshow(sinograma_np, cmap='gray', aspect='auto')
    ax[1].set_title(f'Sinograma {i + 1}')

    plt.show()

    print(f"Reconstrução {i + 1} foi criada e salva como {caminho_reconstrucao}")
