import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import radon
from scipy.ndimage import rotate

#Gere dados de exemplo (sinograma)
theta = np.linspace(0., 180., 180, endpoint=False)
sinogram = np.zeros((180, 100))
sinogram[:, 40:60] = 1

#Reconstrua usando a Transformada de Radon (Scipy)
reconstruction_radon = radon(sinogram, theta=theta, circle=True)
reconstruction_iradon = rotate(reconstruction_radon, angle=90, reshape=False)

#Plote os resultados
plt.figure(figsize=(12, 4))

plt.subplot(131)
plt.title('Sinograma')
plt.imshow(sinogram, cmap='gray', aspect='auto', extent=(0, 100, 180, 0))
plt.colorbar()

plt.subplot(132)
plt.title('Reconstrução Radon (Scipy)')
plt.imshow(reconstruction_iradon, cmap='gray', extent=(0, 100, 0, 100))
plt.colorbar()

plt.show()