import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def read_images(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        img_path = os.path.join(folder_path, filename)
        if os.path.isfile(img_path):
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            images.append((filename, img))  # Armazenar o nome do arquivo junto com a imagem
    return images

def extract_image_number(filename):
    # Extrair o número do nome do arquivo (assumindo que seja o último conjunto de dígitos na string)
    return int(''.join(filter(str.isdigit, filename)))

def plot_images(images):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i, (filename, img) in enumerate(images):
        x = np.arange(img.shape[0])
        y = np.arange(img.shape[1])
        x, y = np.meshgrid(x, y)
        z = np.ones_like(x) * extract_image_number(filename)  # Usar o número extraído do nome do arquivo como coordenada z

        ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=plt.cm.gray(img), shade=False)

    ax.set_zlabel('Image Number')  # Adicionar rótulo ao eixo z
    plt.show()

if __name__ == "__main__":
    folder_path = "C:/Users/Rafa/Documents/Facul/tomografo/transformadas"  # Substitua pelo caminho real para sua pasta de imagens
    images = read_images(folder_path)

    if len(images) < 15:
        print("Número insuficiente de imagens na pasta.")
    else:
        images.sort(key=lambda x: extract_image_number(x[0]))  # Ordenar as imagens pelo número extraído do nome do arquivo
        plot_images(images[:15])  # Plotar apenas as 15 primeiras imagens
