import os

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import radon, iradon
from skimage import io
import time

start_time = time.time()

# Caminho da pasta onde foi salvas as imagens
PastaFotasOriginais = 'F:\\Senac\\4º Semestre\\Fisica Elétrica\\Tomografo\\conjunto 5\\FotosOriginais'

# Caminho da pasta onde ira ser salvas as imagens
PastaFotosProcessadas = 'F:\\Senac\\4º Semestre\\Fisica Elétrica\\Tomografo\\conjunto 5\\FotosProcessadas'

# Caminho de saída para a imagem do sinograma
PastaSinogramas = 'F:\\Senac\\4º Semestre\\Fisica Elétrica\\Tomografo\\conjunto 5\\Sinogramas'

# Pasta de salvamento para os planos axiais
PastaPlanosAxiais = "F:\\Senac\\4º Semestre\\Fisica Elétrica\\Tomografo\\conjunto 5\\PlanosAxiais"

# Definir as coordenadas da área útil a ser recortada (left, top, right, bottom)    
AreaUtil = (196.6 , 0, 210.5, 400)

# Obter uma lista de arquivos na pasta com extensão .jpg
lista_de_imagens = [os.path.join(PastaFotosProcessadas, arquivo) for arquivo in os.listdir(PastaFotosProcessadas) if arquivo.lower().endswith('.jpg')]

# Ordenar a lista de imagens (opcional)
lista_de_imagens.sort()

# Número de imagens por conjunto
imagens_por_conjunto = 200

#Processamento Das Fotos
for FotosTomografos in os.listdir(PastaFotasOriginais):
    # Tons de Cinza
    ArquivoColorido = os.path.join(PastaFotasOriginais, FotosTomografos)
    ImageColorida = Image.open(ArquivoColorido)                                      # Carregar a imagem
    ImagemCinza = ImageColorida.convert('L')                                         # Converter para tons de cinza
    FotosTonsdeCinza = os.path.join(PastaFotosProcessadas, FotosTomografos)          # Construir o caminho para o arquivo de destino em tons de cinza
    ImagemCinza.save(FotosTonsdeCinza)                                               # Salvar a imagem em tons de cinza

    # Densidade Óptica
    ArquivoTonsdeCinza = os.path.join(PastaFotosProcessadas, FotosTomografos)
    ImagemTonsdeCinza = Image.open(ArquivoTonsdeCinza)                               # Carregar a imagem
    ImagemInvertida = Image.eval(ImagemTonsdeCinza, lambda x: 255 - x)               # Inverter óptica (inverter intensidade)
    FotosInvertido = os.path.join(PastaFotosProcessadas, FotosTomografos)            # Construir o caminho para o arquivo de destino invertido
    ImagemInvertida.save(FotosInvertido)                                             # Salvar a imagem invertida

    # Rotacionar
    ArquivoRotacionada = os.path.join(PastaFotosProcessadas, FotosTomografos)
    ImagemRotacionar = Image.open(ArquivoRotacionada)                               # Carregar a imagem
    ImagemGirada = ImagemRotacionar.rotate(-90)                                     # Girar a imagem em 90 graus no sentido horário
    FotosGirado = os.path.join(PastaFotosProcessadas, FotosTomografos)              # Construir o caminho para o arquivo de destino girado
    ImagemGirada.save(FotosGirado)                                                  # Salvar a imagem girada

    # Recortar
    ArquivoRecortado = os.path.join(PastaFotosProcessadas, FotosTomografos)
    Imagem = Image.open(ArquivoRecortado)                                           # Carregar a imagem
    ImagemRecortada = Imagem.crop(AreaUtil)                                         # Recortar a área útil da imagem
    FotosRecortado = os.path.join(PastaFotosProcessadas, FotosTomografos)           # Construir o caminho para o arquivo de destino recortado
    ImagemRecortada.save(FotosRecortado)                                            # Salvar a imagem recortada

print("Processo concluído. As imagens foram salvas na pasta de salvamento dos FotosProcessadas.")

# Sinograma
for Sinograma in range(0, len(lista_de_imagens), imagens_por_conjunto):
    fig, axs = plt.subplots(nrows=1, ncols=imagens_por_conjunto, figsize=(15, 5))   # Configurar o layout do sinograma

    # Loop sobre as imagens no conjunto atual
    for i, indice_imagem in enumerate(range(Sinograma, min(Sinograma + imagens_por_conjunto, len(lista_de_imagens)))):
        caminho_imagem = lista_de_imagens[indice_imagem]
        imagem = Image.open(caminho_imagem)

        array_imagem = np.array(imagem)             # Converter a imagem para um array numpy

        axs[i].imshow(array_imagem, cmap='gray')   # Usado para exibir a imagem no eixo especificado.
        # array_imagem é a representação da imagem como um array NumPy
        # cmap='gray' especifica que a imagem deve ser exibida em escala de cinza.

        axs[i].axis('off') # Desativar a exibição dos eixos (rótulos dos eixos, números dos eixos, etc.) no gráfico

    # Salvar o sinograma como uma imagem
    CaminhoSaida = os.path.join(PastaSinogramas, f"Sinograma{Sinograma // imagens_por_conjunto}.jpg")
    plt.subplots_adjust(wspace = 0)
    plt.savefig(CaminhoSaida, bbox_inches = "tight", pad_inches = 0, dpi = 300)
    # bbox_inches = 'tight' remove qualquer espaço em branco ao redor da imagem
    # pad_inches = 0 garante que não haja preenchimento extra.
    # dpi = 300 define a resolução da imagem em pontos por polegada (dpi)

    plt.close()     # Fechar a figura para liberar recursos

print("Processo concluído. As imagens foram salvas na pasta de salvamento dos Sinogramas.")

# Lista de arquivos na pasta
lista_arquivos = os.listdir(PastaSinogramas)

#Planos Axial
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

    # Ajustar intensidades para evitar fundo branco
    reconstructed_image = (reconstructed_image - np.min(reconstructed_image)) / (np.max(reconstructed_image) - np.min(reconstructed_image))

    # Extraindo apenas o plano axial sem escala
    axial_plane = reconstructed_image[:, :]

    # Exibindo os resultados sem escala e sem eixos
    plt.figure(figsize=(12, 4))

    plt.subplot(133)
    plt.imshow(axial_plane, cmap='gray')
    plt.axis('off')  # Desabilita os eixos

    # Salvar a figura
    nome_figura = f"PlanoAxial_{arquivo[:-4]}.jpg"  # Gera um nome único para cada figura
    caminho_salvamento = os.path.join(PastaPlanosAxiais, nome_figura)
    plt.savefig(caminho_salvamento, bbox_inches = "tight", pad_inches = 0, dpi = 1000)  # Salva sem bordas

    plt.close()  # Fecha a figura para liberar recursos

print("Processo concluído. As imagens foram salvas na pasta de salvamento dos Planos Axiais.")

#Reconstrução 3D


# Registrar o tempo final
end_time = time.time()

# Calcular o tempo decorrido em horas, minutos e segundos
elapsed_time_seconds = end_time - start_time
elapsed_hours = int(elapsed_time_seconds // 3600)
elapsed_minutes = int((elapsed_time_seconds % 3600) // 60)
elapsed_seconds = int(elapsed_time_seconds % 60)

print(f"Tempo decorrido: {elapsed_hours}h {elapsed_minutes} min {elapsed_seconds}s")