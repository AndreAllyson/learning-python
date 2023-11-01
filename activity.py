print("1,2.")
print("*****Olá UNINASSAU*****")
num = int (input("Digite um número: "))
print("O número informado foi", num)

print("3.")
print("*****Impressão e Soma de Números*****")
# Estrutura var = tipo primitivo (função ("texto"))
num1 = int (input ("Digite o primeiro número: "))
num2 = int (input ("Digite o segundo número: "))
res = (num1 + num2)
print ("A soma dos números é: ",res)

print("4.")
print("*****Média das Notas Bimestrais*****")
num1 = float (input ("Digite a nota do 1° bimestre: "))
num2 = float (input ("Digite a nota do 2° bimestre: "))
num3 = float (input ("Digite a nota do 3° bimestre: "))
num4 = float (input ("Digite a nota do 4° bimestre: "))
res = (num1 + num2 + num3 + num4) / 4
print ("A média final das notas é: ", res)

print("5.")
print("*****Conversor de Centímetros para Metros*****")
num1 = float (input ("Digite o valor em metros número: "))
res = (num1 *100)
print ("Na conversão é: ", res)

print("6.")
import math
print("*****Calcular a Área do Circulo*****")
raio = float (input ("Digite o valor do raio do círculo: "))
res = (math.pi * raio**2)
print ("A área do círculo é: ", res)

print("7.")
print("*****Calcular a Área do Quadrado*****")
l = float (input ("Digite o valor do lado do quadrado: "))
res = (l**2)
print (2*res)

print("8.")
print("*****Calcular Salario*****")
sal = float (input("Para saber a quantidade de dinheiro que você ganha por hora, digite o valor de sua remuneração: "))
res = sal/220
print(res)
num = float (input ("Agora que você sabe o valor da remuneração, digite a quantidade de dinheiro que você ganha por hora: "))
num2 = float (input("Digite a quantidade de horas que você trabalhou no mês: "))
result = num * num2
print ("Seu salário mensal é: R$", result)

print("9.")
num = int(input("Digite um número: "))
if num > 0:
 print ("Número positivo")
else:
 print("Número negativo")

print("10.")
resposta = (input ("Digite 'M' - para masculino e 'F' - para femenino: "))
if resposta == 'M' or resposta == 'm':
 print("Masculino")
if resposta == 'F' or resposta == 'f':
 print("Femenino")
else:
 print("Sexo inválido")