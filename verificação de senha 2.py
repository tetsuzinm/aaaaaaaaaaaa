usuario = input("Digite seu usuario: ")
senha = input("Digite sua senha: ")

login_valido = usuario == "admin" and senha == "123456"

if login_valido:
    print("Login realizado com sucesso!")
elif usuario != "admin":
    print("Usuário inválido!")
elif senha != "123456":
    print("Senha inválida!")
else:
    print("Login inválido!")
