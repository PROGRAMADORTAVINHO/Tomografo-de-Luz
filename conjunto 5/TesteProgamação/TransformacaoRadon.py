import os
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import radon
from scipy.ndimage import rotate
from PIL import Image

# Caminho para a pasta contendo os sinogramas
pasta_sinogramas = 'C:\\Users\\jotav\\OneDrive - SENAC - SP\\Área de Trabalho\\4º Semestre\\Fisica Elétrica\\Tomografo\\conjunto 5\\Sinogramas'

# Caminho para a pasta onde as reconstruções serão salvas
pasta_resultados = 'C:\\Users\\jotav\\OneDrive - SENAC - SP\\Área de Trabalho\\4º Semestre\\Fisica Elétrica\\Tomografo\\conjunto 5\\ResconstrucaoRadon'

# Lista todos os arquivos na pasta de sinogramas
arquivos = os.listdir(pasta_sinogramas)

# Itera sobre cada arquivo na pasta de sinogramas
for arquivo in arquivos:
    # Verifica se o arquivo é um sinograma .jpg
    if arquivo.endswith(".jpg"):
        # Caminho completo para o sinograma
        caminho_sinograma = os.path.join(pasta_sinogramas, arquivo)

        # Carrega o sinograma da imagem
        sinogram_image = Image.open(caminho_sinograma)
        sinogram = np.array(sinogram_image.convert('L'))

        # Defina os ângulos theta
        theta = np.linspace(0., 180., sinogram.shape[1], endpoint=False)

        # Reconstrua usando a Transformada de Radon (Scipy)
        reconstruction_radon = radon(sinogram, theta=theta, circle=True)
        reconstruction_iradon = rotate(reconstruction_radon, angle=90, reshape=False)

        # Plote os resultados
        plt.figure(figsize=(12, 4))

        plt.subplot(131)
        plt.title('Sinograma')
        plt.imshow(sinogram, cmap='gray', aspect='auto', extent=(0, sinogram.shape[1], 180, 0))
        plt.colorbar()

        plt.subplot(132)
        plt.title('Reconstrução Radon (Scipy)')
        plt.imshow(reconstruction_iradon, cmap='gray', extent=(0, sinogram.shape[1], 0, sinogram.shape[1]))
        plt.colorbar()

        # Salva a figura na pasta de resultados
        nome_figura = os.path.splitext(arquivo)[0]  # Remove a extensão do arquivo
        caminho_resultado = os.path.join(pasta_resultados, f'{nome_figura}_resultado.png')
        plt.savefig(caminho_resultado)

        # Fecha a figura para liberar recursos
        plt.close()
