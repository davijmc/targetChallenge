import json
import os

# Definindo o caminho do arquivo
caminho_arquivo = os.path.join('C:\\Users\\Davi\\Desktop\\Facul\\targetChallenge', 'dados.json')

# Função para carregar os dados do arquivo JSON
def carregar_dados(caminho):
    with open(caminho, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

# Carregar os dados do arquivo JSON
faturamento = carregar_dados(caminho_arquivo)

# Filtrando os dias com faturamento > 0
valores_validos = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

# Calculando o menor e o maior valor de faturamento
menor_valor = min(valores_validos)
maior_valor = max(valores_validos)

# Calculando a média de faturamento (somente para dias com faturamento > 0)
media_mensal = sum(valores_validos) / len(valores_validos)

# Calculando o número de dias com faturamento superior à média
dias_acima_da_media = sum(1 for dia in valores_validos if dia > media_mensal)

# Exibindo os resultados
print(f"Menor valor de faturamento: {menor_valor:.2f}")
print(f"Maior valor de faturamento: {maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
