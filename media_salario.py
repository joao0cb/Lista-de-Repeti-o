# 3)	Faça um algoritmo que receba como entrada um número indeterminado de salários de indivíduos de uma cidade e escreva a média destes salários.

salario = 1
T_salario = 0
indiv = 0
while salario != 0:
  salario = float(input("Qual o seu salário? "))
  T_salario += salario
  if salario != 0:
    indiv += 1
media = T_salario/indiv
print(f"{media:.2f}")