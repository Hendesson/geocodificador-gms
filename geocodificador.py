import pandas as pd
import googlemaps

# Função para converter decimal para GMS
def decimal_para_gms(valor, direcao_pos, direcao_neg):
    direcao = direcao_pos if valor >= 0 else direcao_neg
    valor = abs(valor)
    graus = int(valor)
    minutos_dec = (valor - graus) * 60
    minutos = int(minutos_dec)
    segundos = round((minutos_dec - minutos) * 60)
    return f"{graus}°{minutos}'{segundos}\"{direcao}"

#  API do Google Maps
API_KEY = 'SUA API AQUI' 

# Inicializar o cliente Google Maps
gmaps = googlemaps.Client(key=API_KEY)

# Caminho do arquivo e aba
arquivo_excel = "seu/caminho/aqui.xlsx"
aba = 'aba_aqui'
df = pd.read_excel(arquivo_excel, sheet_name=aba)

# Função para preencher coordenadas
def preencher_coordenadas(row):
    if pd.isna(row['Latitude']) or pd.isna(row['Longitude']):
        try:
            resultado = gmaps.geocode(row['ENDERECO'])
            if resultado:
                location = resultado[0]['geometry']['location']
                lat = location['lat']
                lon = location['lng']
                lat_gms = decimal_para_gms(lat, 'N', 'S')
                lon_gms = decimal_para_gms(lon, 'E', 'W')
                return pd.Series([lat_gms, lon_gms])
        except Exception as e:
            print(f"Erro ao geocodificar '{row['ENDERECO']}': {e}")
    return pd.Series([row['Latitude'], row['Longitude']])

# Aplicar função
df[['Latitude', 'Longitude']] = df.apply(preencher_coordenadas, axis=1)

# Salvar novo Excel
df.to_excel('planilha_completada_gms.xlsx', index=False)
