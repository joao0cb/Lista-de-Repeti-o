# 6)    Faça um algoritmo que leia um conjunto de 200 alturas em um concurso de beleza e diga a altura da candidata mais alta e da segunda mais alta.

M_altura = 0
S_altura = 0
for i in range(1, 201):
  altura = float(input("Qual a sua altura? "))
  if altura > M_altura:
    S_altura = M_altura
    M_altura = altura

print(f"A altura da(s) candidata(s) mais alta é: {M_altura}")
print(f"A altura da(s) segunda(s) candidatas (s) mais alta é: {S_altura}")