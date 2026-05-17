# Jogo para teste de sorte

import random
import os

nome = os.getlogin().replace(".", " ").title()

while True:
    numero_secreto = random.randint(0, 10)
    tentativas = 1
    vidas = 3
    print(f"\nNovo jogo iniciado!")
    print(f"Você tem apenas 3 tentativas!")
    print(f"{nome}, você deve escolher um número entre 0 e 10")
    while True:
            resposta = input()
            try:
                chute = int(resposta)
                if chute < 0 or chute > 10:
                    print("Serão aceitos apenas número de 0 a 10")
                elif chute < numero_secreto:
                    tentativas += 1
                    vidas -= 1
                    if vidas == 0:
                        print(f"\nInfelizmente você está com muito azar, o número secreto era: {numero_secreto}")
                        break
                    else:
                        print("O número secreto é maior!")
                elif chute > numero_secreto:
                    tentativas += 1
                    vidas -= 1
                    if vidas == 0:
                        print(f"Infelizmente você está com muito azar, o número secreto era: {numero_secreto}")
                        break
                    else:
                        print("O número secreto é menor!")
                else:
                    print(f"Você acertou na {tentativas}º tentativas!\n")
                    break
            except ValueError:
                print("Ei, você deve digitar apenas números!")
    denovo = input("\nDeseja jogar novamente?[s/n]\n")
    if denovo != 's':
        print(f"Valeu por jogar, {nome}! Até a próxima.")
        break
input("\nPresione Enter para sair...")
