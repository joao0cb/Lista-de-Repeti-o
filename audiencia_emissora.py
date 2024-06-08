# 11)

entrevista = "sim"
cultura = 0
sbt = 0
globo = 0
mtv = 0
record = 0
maior_A = 0
menor_A = 9999999999999999

while entrevista.lower() == "sim":
  emissora = input("Qual emissora está sintonizada? ")
  numero_pessoas = int(input("Quantas pessoas estão assistindo? "))
  if emissora.lower() == "cultura":
    cultura += numero_pessoas
  elif emissora.lower() == "sbt":
    sbt += numero_pessoas
  elif emissora.lower() == "globo":
    globo += numero_pessoas
  elif emissora.lower() == "mtv":
    mtv += numero_pessoas
  elif emissora.lower() == "record":
    record += numero_pessoas
  entrevista = input(f"Você deseja continuar as entrevistas? Caso não, escreva 'fim'. ")
total_audiencia = cultura+sbt+globo+mtv+record

if cultura > maior_A:
  maior_A = cultura
elif cultura < menor_A:
  menor_A = cultura
if sbt > maior_A:
  maior_A = sbt
elif sbt < menor_A:
  menor_A = sbt
if globo > maior_A:
  maior_A = globo
elif globo < menor_A:
  menor_A = globo
if mtv > maior_A:
  maior_A = mtv
elif mtv < menor_A:
  menor_A = mtv
if record > maior_A:
  maior_A = record
elif record < menor_A:
  menor_A = record

print(f"A porcentagem de audiência para cada emissora foi de {(cultura/total_audiencia)*100:.2f}% para a Cultura, {(sbt/total_audiencia)*100:.2f}% para o SBT, {(globo/total_audiencia)*100:.2f}% para a Globo, {(mtv/total_audiencia)*100:.2f}% para o MTV e {(record/total_audiencia)*100:.2f}% para a Record.")
print(f"A maior audiência foi de {maior_A:.2f} pessoas.")
print(f"A menor audiência foi de {menor_A:.2f} pessoas.")