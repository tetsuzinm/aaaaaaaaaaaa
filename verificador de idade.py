#igual ou maior que 18 anos de idade é adulto

idade = int(input("Qual a sua idade: "))
verificador =  idade >= 18

print(verificador)


#Para dirigir a pessoa tem que ser igual ou maior que 18 anos de idade e ter a carteira de motorista

idade = int(input("Qual a sua idade: "))
carterira = True
verificador = idade >= 18 and carterira

print(verificador)

#segunda versão

idade = int(input('Qual sua idade? '))
autorizacao_pais = input('Você tem autorização dos seus pais? (sim/não) ')

if idade >= 18:
    print('Você pode entrar na festa.')
elif idade >= 16 and autorizacao_pais == 'sim':
    print('Você pode entrar na festa com autorização dos pais.')
else:
    print('Você não pode entrar na festa.')
