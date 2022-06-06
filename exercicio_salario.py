salario = input ('digite seu salário: ')
salario = float(salario)

gasto = input ('digite seu gasto: ')
gasto = float(gasto)

salario_total = salario * 12
gasto_total  = gasto * 12

economizado = salario_total - gasto_total

print("você pode economizar até o fim do ano o valor de" , economizado)
