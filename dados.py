# 7)

contH =0
altura_h = 0
a = 0
b = 0
peso_M = 0
contM = 0
peso_H90 = ''
idade_H = ''
h_alto = ''
m_peso = ''
m_idade = ''

for i in range(1, 150):
  nome = input("Nome: ")
  altura = float(input("Altura: "))
  peso = float(input("Peso: "))
  idade = int(input("Idade: "))
  genero = input("Gênero: ")

  if genero.lower() == "homem":
    altura_h += altura
    contH += 1
    if altura > a:
      a = altura
      h_alto = nome
    elif altura == a:
      h_alto += f"{nome}\n"
    if idade > 50:
      idade_H += f"{nome}\n"
    if peso > 90:
      peso_H90 += f"{nome}\n"

  if genero.lower() == "mulher":
    peso_M += peso
    contM += 1
    if peso > b:
      b = peso
      m_peso += nome
    elif peso == b:
      m_peso += f"{nome}\n"
    if idade < 18:
      m_idade += f"{nome}\n"

media_alturaH = altura_h/contH
print(f"Média das alturas dos homens:\n{media_alturaH:.2f}")
print(f"Nome do(s) homem(ns) mais alto(s):\n{h_alto}")
print(f"Nome dos homens com mais de 50 anos:\n{idade_H}")
print(f"Nome dos homens com mais de 90Kg:\n{peso_H90}")
media_pesoM = peso_M/contM
print(f"Média dos pesos das mulheres:\n{media_pesoM:.2f}")
print(f"Nome da(s) mulher(es) mais gorda(s):\n{m_peso}")
print(f"Nome das mulheres menor de idade:\n{m_idade}")