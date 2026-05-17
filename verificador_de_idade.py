name = input(f"Qual seu nome?\n")

while True:
    resposta = input(f"{name}, qual sua idade?\n")
    try:
        idade = int(resposta)
        if idade >= 120:
                print(f"Acredito que você não é uma mumia")
        else:
            break
    except ValueError:
        print(f"Erro, porfavor, digite apenas números!")

if idade <= 17:
    print(f"Poxa {name}, você é menor de idade.")
else:
    print(f"Que legal {name}, você é maior de idade!")
