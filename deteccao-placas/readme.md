
# Projeto de Reconhecimento de Placas Veiculares

Projeto criado para a disciplina Fundamentos de Inteligência Artificial (FIA) - Graduação. Professor: Pablo De Chiaro  

Este projeto utiliza técnicas de Visão Computacional e Reconhecimento Óptico de Caracteres (OCR) para detectar e reconhecer placas veiculares em imagens.

## Configuração do Ambiente Virtual

### Passos para criar e ativar o ambiente virtual:

1. **Criar o ambiente virtual:**  
   Execute o seguinte comando no terminal:  

   ```bash
   python -m venv env-placas
   ```

2. **Ativar o ambiente virtual:**  

   No macOS e Linux:

   ```bash
   source ./env-placas/bin/activate
   ```

   No Windows:

   ```bash
   .\env-placas\Scripts\activate
   ```

## Instalação de Dependências

Certifique-se de que o ambiente virtual esteja ativado. Em seguida, instale as dependências do projeto utilizando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Conteúdo do arquivo `requirements.txt`:

```text
numpy==2.0.0
opencv-python==4.10.0.84
pytesseract==0.3.10
```

## Configuração do Tesseract OCR

1. **Instalar o Tesseract OCR:**  
   Baixe e instale o Tesseract OCR no seu sistema. Ele pode ser encontrado [aqui](https://github.com/tesseract-ocr/tesseract).

2. **Configurar o caminho do executável (Windows):**  
   Ajuste o caminho no código, como mostrado abaixo:

   ```python
   pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
   ```

## Como Executar

O código principal está no arquivo `detectar_placa.py`. Para rodar o projeto, certifique-se de que há imagens na pasta `deteccao-placas/images` e execute o comando:

```bash
python detectar_placa.py
```

O script irá processar todas as imagens da pasta e exibir os resultados.

### Estrutura do Projeto

```plaintext
/
├── detectar_placa.py             # Código principal do projeto
├── processar_imagem.py           # Processamento de imagem (pré-processamento)
├── processar_contornos.py        # Extração de contornos
├── aplicar_ocr.py                # Aplicação de OCR
├── utils.py                      # Funções auxiliares para exibir os resultados
├── deteccao-placas/
│   └── images/                   # Pasta com imagens para teste
├── requirements.txt              # Dependências do projeto
└── README.md                     # Documentação do projeto
```

## Verificação da Instalação

Para garantir que tudo foi instalado corretamente, execute o seguinte código no Python:

```python
import cv2
import numpy as np
import pytesseract

print(f"OpenCV version: {cv2.__version__}")
print(f"NumPy version: {np.__version__}")
print(f"Pytesseract version: {pytesseract.get_tesseract_version()}")
```

## Funcionalidades Implementadas

- **Pré-processamento de imagens:** Ajuste de contraste, remoção de ruído, conversão para escala de cinza.
- **Detecção de contornos:** Identificação de regiões que podem conter placas.
- **Recorte e análise de placas:** Seleção da região e extração de texto usando OCR.
- **Visualização:** Exibição das imagens com as placas destacadas e o texto reconhecido.

## Sugestão de Estudos por Diretórios

1. `processar_imagem.py` - Trabalhe no pré-processamento para melhorar a qualidade das imagens.
2. `processar_contornos.py` - Ajuste os critérios de detecção de contornos.
3. `aplicar_ocr.py` - Experimente diferentes configurações do Tesseract para melhorar o OCR.
4. `utils.py` - Personalize a exibição dos resultados.

## Desativação do Ambiente Virtual

Ao finalizar o trabalho, você pode desativar o ambiente virtual com:

```bash
deactivate
```

## Referências e Leitura

- [Documentação OpenCV](https://docs.opencv.org/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Artigo sobre OCR com Python](https://medium.com/@techmayank2000/using-tesseract-with-python-for-ocr)

Este projeto é apenas um ponto de partida para o desenvolvimento de sistemas de reconhecimento de placas veiculares. Explore e personalize conforme suas necessidades!
