print("Vamos calcular!")
while True:
            try:
                num1 = float(input("Digite o primeiro número: "))
                opr = input("Digite a operação (+, -, *, /): ")
                num2 = float(input("Digite o segundo número: "))
                if num2 == 0 and opr == '/':
                    print("Não é possível dividir por zero!")
                    continue
                elif opr == '+':
                    resposta = num1 + num2
                elif opr == '-':
                    resposta = num1 - num2
                elif opr == '*':
                    resposta = num1 * num2
                elif opr == '/':
                    resposta = num1 / num2
                else:
                    print(f"ERRO: '{opr}' não é uma operação válida, escolha entre (+, -, *, /)!")
                    continue
                print(f"\nO resultado da sua conta é: {resposta}")
            except ValueError:
                print("Por favor, digite apenas NÚMEROS.")
                continue
            sair = input("Você deseja realizar outro calculo? (s/n): ")
            if sair == 'n':
                break
            else:
                print("Continuando...\n")
                continue
input("\nObrigado por usar minha calculadora, aperte enter para sair.")
