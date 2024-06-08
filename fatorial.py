# 5)	Faça um algoritmo que calcule o fatorial de um valor qualquer fornecido pelo usuário.

valor = int(input("Insira um valor: "))
for i in range(1, valor):
  valor *= i
print(valor)