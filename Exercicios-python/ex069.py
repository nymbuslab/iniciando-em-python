"""
Crie um programa que faça o computador jogar
JOKENPO com você.
"""

from random import choice
import time

nome_jogo = "JOKENPÔ"
computador = choice(["Pedra", "Papel", "Tesoura"])
jogador = input("Escolha entre PEDRA, PAPEL ou TESOURA: ").strip().title()


if jogador not in ["Pedra", "Papel", "Tesoura"]:
    resultado = "Jogada inválida!"
elif jogador == computador:
    resultado = "Empate!"
elif (jogador == "Pedra" and computador == "Tesoura") or \
     (jogador == "Papel" and computador == "Pedra") or \
     (jogador == "Tesoura" and computador == "Papel"):
    resultado = f"Você ganhou! Eu escolhi {computador} e você {jogador}"
else:
    resultado = f"Eu ganhei! Eu escolhi {computador} e você {jogador}"
    
print("\n")
print("-=-" * 10)
print(f"{nome_jogo: ^30}")
print("-=-" * 10)
print("\n")
print("Vamos começar?")
print("JO...")
time.sleep(2)
print("KEN...")
time.sleep(2)
print("PÔ...")
time.sleep(2)
print(resultado)
