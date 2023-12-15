import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.transform import iradon

# Função para realizar a transformada de Radon inversa em uma imagem
def iradon_transform(sinogram):
    reconstruction = iradon(sinogram, circle=True)
    
    return reconstruction

# Pasta de entrada e saída
input_folder = 'F:\\Senac\\4º Semestre\\Fisica Elétrica\\Tomografo\\conjunto 5\\Sinogramas'
output_folder = 'F:\\Senac\\4º Semestre\\Fisica Elétrica\\Tomografo\\conjunto 5\\PlanosAxiais'

# Garante que a pasta de saída existe
os.makedirs(output_folder, exist_ok=True)

# Itera sobre os sinogramas na pasta de entrada
for i in range(1, 16):
    # Carrega o sinograma
    sinogram_path = os.path.join(input_folder, f'sinograma_{i}.png')
    sinogram = cv2.imread(sinogram_path, cv2.IMREAD_GRAYSCALE)

    # Realiza a transformada de Radon inversa com ajuste de gamma
    reconstruction = iradon_transform(sinogram)

    # Normaliza os valores da imagem para o intervalo [0, 255]
    reconstruction_normalized = (reconstruction - np.min(reconstruction)) / (np.max(reconstruction) - np.min(reconstruction)) * 255
    
    # Inverte as intensidades para que as partes mais densas sejam brancas
    reconstruction_normalized = 73 - reconstruction_normalized.astype(np.uint8)

    # Plota os sinogramas
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(sinogram, cmap='gray')
    plt.title(f'Sinograma {i}')

    # Exibe a reconstrução com ajuste de gamma
    plt.subplot(1, 2, 2)
    plt.imshow(reconstruction_normalized, cmap='gray')
    plt.title(f'Reconstrução {i}')

    # Exibe os gráficos
    plt.show()

    # Salva as imagens resultantes
    output_path = os.path.join(output_folder, f'reconstrucao_{i}.png')
    plt.imsave(output_path, reconstruction_normalized, cmap='gray')

