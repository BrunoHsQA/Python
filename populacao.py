dados_cidade = {
'nome' : 'São Paulo' ,
'estado': 'São Paulo' ,
'area_km2' : 1521 ,
'pop_milhoes' : 13
}

print(type(dados_cidade))


print(dados_cidade)

dados_cidade['país'] = 'Brasil'

print(dados_cidade)

print(dados_cidade['nome'])

dados_cidade['area_km2'] = 1500

print(dados_cidade)


dados_cidade_2 = dados_cidade

dados_cidade_2 ['nome'] = 'Santos'

print(dados_cidade)

dados_cidade_3 = dados_cidade.copy()

dados_cidade_3 ['estado'] = 'Rio de Janeiro'

print(dados_cidade)

novos_dados = {'pop_mi': 15,
               'fundacao' : '25/01/1554'}

dados_cidade.update(novos_dados)

print(dados_cidade)

print(dados_cidade.get('prefeito'))


print(dados_cidade.keys())
print()
print(dados_cidade.values())
print()
print(dados_cidade.items())
