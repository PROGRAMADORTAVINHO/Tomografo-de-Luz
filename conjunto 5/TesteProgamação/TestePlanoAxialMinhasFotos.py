import os
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import radon, iradon
from skimage import io

# Pasta contendo as imagens
PastaSinogramas = "C:\\Users\\jotav\\OneDrive - SENAC - SP\\Área de Trabalho\\4º Semestre\\Fisica Elétrica\\Tomografo\\conjunto 5\\Sinogramas"

# Lista de arquivos na pasta
lista_arquivos = os.listdir(PastaSinogramas)

# Iterar sobre cada arquivo na pasta
for arquivo in lista_arquivos:
    caminho_imagem = os.path.join(PastaSinogramas, arquivo)

    # Carregar a imagem
    sinogram = io.imread(caminho_imagem, as_gray=True)

    # Parâmetros da imagem de teste
    image_size = 128
    num_projections = sinogram.shape[1]  # Obtendo o número de projeções do sinograma
    theta = np.linspace(0., 180., num_projections, endpoint=False)
    image = np.zeros((image_size, image_size))
    image[:, image_size // 4:3 * image_size // 4] = 1

    # Reconstrução usando o sinograma carregado
    reconstructed_image = iradon(sinogram, theta=theta, circle=False)

    # Exibindo os resultados
    plt.figure(figsize=(12, 4))

    plt.subplot(133)
    plt.title("Imagem Reconstruída")
    plt.imshow(reconstructed_image, cmap='gray')

    # Salvar a figura
    nome_figura = f"resultado_{arquivo[:-4]}.png"  # Gera um nome único para cada figura
    caminho_salvamento = os.path.join("C:\\Users\\jotav\\OneDrive - SENAC - SP\\Área de Trabalho\\4º Semestre\\Fisica Elétrica\\Tomografo\\conjunto 5\\PlanosAxiais", nome_figura)
    plt.savefig(caminho_salvamento)

    plt.close()  # Fecha a figura para liberar recursos

print("Processo concluído. As imagens foram salvas na pasta de salvamento.")