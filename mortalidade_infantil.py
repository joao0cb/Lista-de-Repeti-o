# 10)

total_criancas = int(input("Quantas crianças nasceram no período? "))

criancas_mortas = 0
mortas_feminino = 0
mortas_24meses = 0
sexo = "feminino"

while sexo != "vazio":
  sexo = input("Digite o sexo da criança morta. Digite 'vazio' para encerrar. ")
  criancas_mortas += 1
  if sexo == "feminino" or sexo == "masculino":
    if sexo == "feminino":
      mortas_feminino += 1
    meses_vida = int(input("Quantos meses de vida a criança teve? "))
    if meses_vida <= 24:
     mortas_24meses += 1

print(f"A porcentagem de crianças mortas no período foi de {(criancas_mortas/total_criancas)*100:.2f}%.")
print(f"A porcentagem de crianças do sexo feminino mortas no período foi de {(mortas_feminino/total_criancas)*100:.2f}%.")
print(f"A porcentagem de crianças que viveram 24 meses de vida ou menos foi de {(mortas_24meses/total_criancas)*100:.2f}%.")