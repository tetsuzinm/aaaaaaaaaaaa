#igual ou maior que 18 anos de idade é adulto

idade = int(input("Qual a sua idade: "))
verificador =  idade >= 18

print(verificador)


#Para dirigir a pessoa tem que ser igual ou maior que 18 anos de idade e ter a carteira de motorista

idade = int(input("Qual a sua idade: "))
carterira = True
verificador = idade >= 18 and carterira

print(verificador)
