# 1)

for i in range(1, 501):
  salario = float(input("Qual o seu salário? "))
  if salario <= 1600:
    print("Você está isento de imposto.")
  elif salario > 1600 and salario <= 3000:
    imposto = (salario/100)*10
    print(f"O valor do imposto a ser pago é R${imposto:.2f}")
  elif salario > 3000 and salario <= 7000:
    imposto = (salario/100)*15
    print(f"O valor do imposto a ser pago é R${imposto:.2f}")
  else:
    imposto = (salario/100)*20
    print(f"O valor do imposto a ser pago é R${imposto:.2f}")