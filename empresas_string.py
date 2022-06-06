nome_cidade = input("Qual a cidade litorânea começa com a letra 'C'?")

nome_cidade = nome_cidade.strip()

while nome_cidade.lower() != 'caraguatatuba':
    print('errado.')
    nome_cidade = input("Qual a cidade litorânea começa com a letra 'C'?")


print('Acertou')
