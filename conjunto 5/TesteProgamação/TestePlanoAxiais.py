import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import radon, iradon
from skimage import io

# Carregando um sinograma a partir de um arquivo de imagem
sinogram_path = "C:\\Users\\jotav\\OneDrive - SENAC - SP\\Área de Trabalho\\4º Semestre\\Fisica Elétrica\\Tomografo\\conjunto 5\\Teste\\Sinograma5.jpg"
sinogram = io.imread(sinogram_path, as_gray=True)

# Parâmetros da imagem de teste
image_size = 128
num_projections = sinogram.shape[1]  # Obtendo o número de projeções do sinograma
theta = np.linspace(0., 180., num_projections, endpoint=False)
image = np.zeros((image_size, image_size))
image[:, image_size//4:3*image_size//4] = 1

# Reconstrução usando o sinograma carregado
reconstructed_image = iradon(sinogram, theta=theta, circle=False)

# Exibindo os resultados
plt.figure(figsize=(12, 4))

plt.subplot(132)
plt.title("Sinograma")
plt.imshow(sinogram, cmap='gray', extent=(0, 180, 0, sinogram.shape[0]), aspect='auto')

plt.subplot(133)
plt.title("Imagem Reconstruída")
plt.imshow(reconstructed_image, cmap='gray')

plt.show()