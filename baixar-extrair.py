import requests
import os
import zipfile


# Lista de meses em formato de 2 dígitos numéricos (01 a 12)
meses = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

# User-Agent do Firefox
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'

# Loop para baixar os arquivos para cada mês
for mes in meses:
    # URLs para os arquivos de pagamentos e saques
    url_pagamentos = f'https://dadosabertos-download.cgu.gov.br/PortalDaTransparencia/saida/bolsa-familia-pagamentos/2020{mes}_BolsaFamilia_Pagamentos.zip'
    url_saques = f'https://dadosabertos-download.cgu.gov.br/PortalDaTransparencia/saida/bolsa-familia-saques/2020{mes}_BolsaFamilia_Saques.zip'

    # Lista de URLs a serem baixadas
    urls = [url_pagamentos, url_saques]


    for url in urls:
        # Defina o cabeçalho User-Agent
        headers = {'User-Agent': user_agent}

        # Faça a solicitação HTTP com o User-Agent simulado
        response = requests.get(url, headers=headers)

        # Verifique se a solicitação foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            # Nome do arquivo a ser salvo
            nome_arquivo = url.split('/')[-1]

            # Salve o arquivo no disco
            with open(nome_arquivo, 'wb') as arquivo:
                arquivo.write(response.content)

            print(f'Arquivo {nome_arquivo} baixado com sucesso!')
        else:
            print(f'Falha ao baixar o arquivo {url}. Status code: {response.status_code}')

# for file in *.zip; do unzip "$file" -d "${file%.zip}"; done

# Obtenha a lista de arquivos .zip no diretório atual
arquivos_zip = [arquivo for arquivo in os.listdir() if arquivo.endswith('.zip')]

# Loop pelos arquivos .zip e descompacte-os
for arquivo_zip in arquivos_zip:
    nome_pasta_destino = os.path.splitext(arquivo_zip)[0]  # Remove a extensão .zip
    with zipfile.ZipFile(arquivo_zip, 'r') as zip_ref:
        zip_ref.extractall(nome_pasta_destino)
    print(f'Arquivo {arquivo_zip} descompactado para {nome_pasta_destino}')