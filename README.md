# 🗺️ Geocodificador GMS com Google Maps API

Este repositório contém um script em Python que automatiza o preenchimento de coordenadas geográficas (latitude e longitude) a partir de endereços presentes em uma planilha Excel. As coordenadas são convertidas do formato decimal para o formato GMS (graus, minutos e segundos).

## 🚀 Funcionalidades

- Geocodifica endereços utilizando a API do Google Maps.
- Converte coordenadas decimais para o formato GMS.
- Exporta a planilha original com colunas atualizadas de latitude e longitude.
- Trata erros de geocodificação de forma segura.

## 📁 Estrutura esperada da planilha

A planilha Excel usada como entrada deve conter ao menos uma coluna chamada `ENDERECO`. As colunas `Latitude` e `Longitude` também devem existir (podem estar vazias).

Exemplo:

| ENDERECO                              | Latitude | Longitude |
|---------------------------------------|----------|-----------|
| Rua Henrique Dias, 162, Rio Branco...|          |           |

## ⚙️ Requisitos

- Python 3.8+
- Conta com chave de API do Google Maps

### 📦 Bibliotecas utilizadas

- `pandas`
- `googlemaps`

