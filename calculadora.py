print('------------------------')
print('|Bem-vido a calculadora|')
print('------------------------')

print('   ')

print("==== Escolha a operação ====")
print("|1 -      Soma (+)         |")
print("|2 -     Divisão (/)       |")
print("|3 -    Multiplicação (*)  |")
print("|4 -     Subtração (-)     |")
print("============================")

operacao = input(':')

numero1 = int(input('Digite o peimeiro numero:'))
numero2 = int(input('Digite o segundo numero:'))

print('   ')

if operacao == '+':
  print ('O resultado é:', numero1 + numero2)

elif operacao == '/':
  print ('O resultado é:', numero1 / numero2)

elif operacao == '*':
  print ('O resultado é:', numero1 * numero2)

elif operacao == '-':
  print ('O resultado é:', numero1 - numero2)

else:
  print('Operação invalida')
