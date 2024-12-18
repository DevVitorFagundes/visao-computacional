import os
import cv2
from processar_imagem import processar_imagem
from processar_contornos import processar_contornos
from aplicar_ocr import aplicar_ocr
from utils import exibir_resultado
import pytesseract

# Configurar o caminho do executável Tesseract (se necessário)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR/tesseract.exe'

def detectar_placa(imagem_path):
    imagem_original = cv2.imread(imagem_path)
    if imagem_original is None:
        print(f"Erro ao carregar a imagem: {imagem_path}")
        return
    
    imagem_processada = processar_imagem(imagem_original)
    possiveis_placas = processar_contornos(imagem_original, imagem_processada)

    if len(possiveis_placas) == 0:
        print("Nenhuma placa encontrada.")
        return

    placa_detectada, placa_recortada, placa_recortada_processada = aplicar_ocr(possiveis_placas)

    exibir_resultado(imagem_original, imagem_processada, placa_recortada,
                     placa_recortada_processada, placa_detectada)

if __name__ == "__main__":
    pasta_imagens = "deteccao-placas/images"
    
    if not os.path.exists(pasta_imagens):
        print(f"Erro: A pasta '{pasta_imagens}' não foi encontrada.")
        exit(1)

    lista_imagens = os.listdir(pasta_imagens)

    for imagem_file in lista_imagens:
        if not imagem_file.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue

        imagem_path = os.path.join(pasta_imagens, imagem_file)
        print(f"Processando: {imagem_file}")
        detectar_placa(imagem_path)
