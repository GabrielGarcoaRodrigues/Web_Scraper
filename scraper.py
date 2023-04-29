import requests
from bs4 import BeautifulSoup

# Passando a url do produto desejado
url = 'https://www.netshoes.com.br/mini-bola-de-basquete-wilson-nba-dribbler-marrom-D25-3846-138'  # <--- Informe a url do produto

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}                                # <---  Evitar problemas de permissão

# Pegando o html da página do produto
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
produto = soup.select_one('main')

# Extraindo as informaçoes do produto
nome = produto.select_one('h1').text
preco = produto.select_one('div.default-price').text
imagem = produto.select_one('img.zoom')['src']
descricao = produto.select_one('.description').text.strip()

# Print das informaçoes extraidas
print("Nome do produto:", nome)
print("Preço do produto:", preco)
print("Imagem do produto:", imagem)
print("Descrição do produto:", descricao)
