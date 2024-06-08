#4)	Escrever um algoritmo que calcule a média obtida por uma turma de "n" alunos na primeira prova do semestre.

soma_notas = 0
alunos = int(input("Quantos alunos tem na turma? "))
for i in range(1, alunos+1):
  nota = float(input("Nota do aluno: "))
  soma_notas += nota
media_notas = soma_notas/alunos
print(f"{media_notas:.2f}")