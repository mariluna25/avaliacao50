"""
#1) Criar uma lista de 5 nomes e 5 idades

listaNomes=["Jão", "Pedro", "Maria", "Luna", "Joana"]
listaIdade=[8,10,12,9,11]
print(listaNomes)

#2) Acrescentar mais 2 nomes nesta lista

listaNomes.extend(["Paula", "Carlos"])
print(listaNomes)
"""
"""
#3) Receber um nome e 3 notas calcular a média final se a média  for maior que 7 aprovado senão reprovado

input("Nome do Aluno:")
a= float(input("Av1:"))
b= float(input("Av2:"))
c= float(input("Av3:"))
m= float(print("Média Final:", (a+b+c)/3))

if m>=7.0:
    print("APROVADO")
else:
    print("REPROVADO")
"""
"""
#4) Criar um algoritmo que receba o salario de um funcionário e informe a ele o valor de desconto
# do INSS e seu salário Líquido

salario= float(input("Digite o valor do seu salário:R$"))
if salario<=1212:
    print("Desconto do INSS será de 7,5%")
    print("Salário Líquido:R$",salario - (salario*7.5/100))
if salario>1212 or salario<=2427.35:
    print("Desconto DO INSS será de 9%")
    print("Salário Líquido:R$", salario-(salario*9/100))
if salario>2427.35 or salario<=3641.03:
    print("Desconto DO INSS será de 12%")
    print("Salário Líquido:R$", salario - (salario*12/100))
if salario>3641.03 or salario<=7087.22:
    print("Desconto DO INSS será de 14%")
    print("Salário Líquido:R$", salario-(salario*14/100))
"""
"""
#5) Criar um algoritmo que receba dois valores e pergunte ao
#usuário qual tipo de cálculo deseja que seja feito. (soma
#Subtração, multiplicação ou divisão) com a indicação do usuário
#efetuar a operação matemática

print("Digite dois valores:")
a=int(input())
b=int(input())
c= input("Qual cálculo deseja fazer: soma, subtração, multiplicação ou divisão?")
if c=="soma":
    print("Resultado=", a+b)
if c=="subtração":
    print("Resultado=", a-b)
if c=="multiplicação":
    print("Resultado=", a*b)
if c=="divisão":
    print("Resultado=", a/b)
"""
"""
#6) criar um programa que calcule celsius para farenheit e ao contrário também
print("Conversor de Temperatura")
c= float(input("Digite a temperadura em graus Celsius:"))
print("Em Fahrenheint=", c*1.8+32)
f= float(input("Digite a temperatura em Fahrenheint:"))
print("Em Celsius=", (f-32)/1.8)
"""
"""
#7) Receba o nome do aluno, três notas (trab(4), teste(3), prova(5))
#vai calcular média poderada exibir a média

input("Nome do Aluno:")
trab = float(input("Nota trabalho:"))
teste = float(input("Nota teste:"))
prova = float(input("Nota prova:"))
print("Média:",(trab*4)+(teste*3)+(prova*5)/4+3+5)
"""
"""
#8) tabuada de acordo com a escolha do cliente e ao final
#perguntar se ele deseja uma nova tabuada

valor= int(input("Qual número deseja a tabuada?"))
n=0
while n<=10:
    print(f"{n} x {valor} =", valor*n)
    n=n+1

resp= input("Deseja uma nova tabuada?")
while resp== "sim":
    valor = int(input("Qual número deseja a tabuada?"))
    n = 0
    while n <= 10:
        print(f"{n} x {valor} =", valor * n)
        n = n + 1
    resp = input("Deseja uma nova tabuada?")
else:
    print("Fim da Tabuada!")
"""
