# 8) Escrever um algoritmo que lê um número desconhecido de valores, um de cada vez, e conta quantos deles estão em cada um dos intervalos [0,25], (25,50], (50,75], (75,100].

a025 = 0
b2550 = 0
c5075 = 0
d75100 = 0
valor = 0

while valor >= 0 and valor <= 100:
  valor = float(input("Valor: "))
  if valor >= 0 and valor <= 25:
    a025 += 1
  elif valor > 25 and valor <= 50:
    b2550 += 1
  elif valor > 50 and valor <= 75:
    c5075 += 1
  elif valor > 75 and valor <= 100:
    d75100 += 1

print(f"Existem {a025:.2f} valores entre 0 e 25, {b2550:.2f} entre 25 e 50, {c5075:.2f} entre 50 e 75 e {d75100:.2f} entre 75 e 100.")