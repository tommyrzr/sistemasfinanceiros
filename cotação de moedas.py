#pip install httpx

import httpx

moeda_base = input('Digite a moeda de base: ').upper()
moeda = input('Digite a moeda desejada: ').upper()
valor_da_moeda= float(input('Digite o valor que deseja saber: '))

response = httpx.get(url=f'https://api.exchangerate.host/latest?base={moeda_base}').json()

dados_da_moeda = response['rates']



valor_da_moeda_base = dados_da_moeda.get(moeda)
valor_calculado = valor_da_moeda_base * valor_da_moeda



print(f'{valor_da_moeda} {moeda_base} vale {valor_calculado} {moeda}')
