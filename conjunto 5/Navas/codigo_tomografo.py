from PIL import Image
from skimage import transform, util
import os

# Caminho para a pasta contendo as imagens
caminho_pasta = "F:\\Senac\\4º Semestre\\Fisica Elétrica\\Tomografo\\conjunto 5\\FotosOriginais"
caminho_saida = "F:\\Senac\\4º Semestre\\Fisica Elétrica\\Tomografo\\conjunto 5\\FotosProcessadas"

# Cria o diretório de saída se não existir
if not os.path.exists(caminho_saida):
    os.makedirs(caminho_saida)

# Lista todos os arquivos na pasta
arquivos = os.listdir(caminho_pasta)

# Loop sobre cada arquivo na pasta
for arquivo in arquivos:
    # Verifica se o arquivo é uma imagem jpg
    if arquivo.lower().endswith(".jpg"):
        # Caminho completo para a imagem
        caminho_imagem = os.path.join(caminho_pasta, arquivo)

        # Carrega a imagem usando Pillow
        imagem_pillow = Image.open(caminho_imagem)

        # Converte a imagem para escala de cinza
        imagem_cinza = imagem_pillow.convert("L")

        # Converte a imagem Pillow de volta para um array NumPy para uso com scikit-image
        imagem_cinza_np = util.img_as_ubyte(imagem_cinza)

        # Rotaciona a imagem em 90 graus
        imagem_rotacionada = transform.rotate(imagem_cinza_np, 89.2, resize=False, preserve_range=True).astype(imagem_cinza_np.dtype)

        # Inverte a densidade ótica (subtrai cada valor de pixel da intensidade máxima possível)
        imagem_invertida = util.invert(imagem_rotacionada)

        # Corta a imagem removendo 3 pixels na parte superior
        imagem_cortada = Image.fromarray(imagem_invertida[3:-5, 195:-200])

        # Salva a imagem cortada em outro diretório
        caminho_imagem_cortada = os.path.join(caminho_saida, f"{arquivo}")
        imagem_cortada.save(caminho_imagem_cortada)
