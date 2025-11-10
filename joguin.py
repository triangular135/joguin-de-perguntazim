
import random

print("Bem-vindo ao jogo de adivinhação!")
palavra_secreta = random.choice(['maçã', 'banana', 'laranja', 'uva', 'melancia', 'abacaxi'])
tentativas = 0
while True:
    palpite = input("Digite o nome de uma fruta entre maçã, banana, laranja, uva, melancia e abacaxi : ")
    tentativas += 1
    if palpite == palavra_secreta:
        print(f"Parabéns! Você adivinhou a fruta secreta em {tentativas} tentativas.")
        break
    else:
        print("Fruta incorreta. Tente novamente.")

    
