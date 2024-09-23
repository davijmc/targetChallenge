dados = [{"Estado": "SP", "Valor": 67836.43}, {"Estado": "RJ", "Valor": 36678.66}, {"Estado": "MG", "Valor": 29229.88}, {"Estado": "ES", "Valor": 27165.48}, {"Estado": "Outros", "Valor": 19849.53}]

# Calculando o percentual que cada estado representa
total = sum(dado['Valor'] for dado in dados)
for dado in dados:
    percentual = (dado['Valor'] / total) * 100
    print(f"{dado['Estado']}: {percentual:.2f}%")