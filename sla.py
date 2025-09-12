produto = float(input("Digite quantos produtos vc compra: "))
uso = float(input("Digite quanto vc usa: "))
dias = int(input("Digite quantos dias vc usa: "))

novo = produto - uso * dias
print(f'vc usa {novo}')
