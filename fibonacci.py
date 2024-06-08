# 9)

f_anterior = 1
f_atual = 1
soma = 2
print(f_anterior)
print(f_atual)
for i in range(2, 100):
  proximo_f = f_atual + f_anterior
  soma += proximo_f
  f_anterior = f_atual
  f_atual = proximo_f
  print(proximo_f)
print(f"\nA soma de todos esses termos é {soma}.")