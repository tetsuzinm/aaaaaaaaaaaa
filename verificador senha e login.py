usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

login_valido = usuario == 'Admin' and senha == '123456'

print(f'login_valido: {login_valido}')
