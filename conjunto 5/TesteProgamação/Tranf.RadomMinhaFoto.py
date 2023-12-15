import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import radon
from scipy.ndimage import rotate
from PIL import Image

# Carregue o sinograma real em formato .jpg
sinogram_image = Image.open('C:\\Users\\jotav\\OneDrive - SENAC - SP\\Área de Trabalho\\4º Semestre\\Fisica Elétrica\\Tomografo\\conjunto 5\\Teste\\Sinograma5.jpg')
sinogram = np.array(sinogram_image.convert('L'))  # Converte para escala de cinza

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

plt.show() 