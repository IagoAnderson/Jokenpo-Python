# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
#Iago Anderson Pereira file
import random
from time import sleep

jogadas = ['Pedra', 'Papel', 'Tesoura']
computador = ''
jogador = ''
placar_jogador = 0
placar_computador = 0
jogo = 0

print("Seja muito bem vindo ao Jokenpô")

while jogo < 5:
    computador = random.choice(jogadas)
    jogador = int(input('(1) - Pedra\n(2) - Papel\n(3) - Tesoura\nFaça sua jogada: '))
    if jogador != 1 and jogador != 2 and jogador != 3:
        print('Opção inválida!')
        sleep(2)
        break
    print(f'O computador escolheu \033[35m{computador}\033[m')
    if jogador == 1:
        jogada = 'Pedra'
    elif jogador == 2:
        jogada = 'Papel'
    elif jogador == 3:
        jogada = 'Tesoura'
    print(f'O jogador escolheu \033[34m{jogada}\033[m')
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    if jogador == 1 and computador == 'Pedra' or jogador == 2 and computador == 'Papel' or jogador == 3 and computador == 'Tesoura':
        print('\033[33mEmpate!\033[m')
    elif jogador == 3 and computador == 'Papel' or jogador == 1 and computador == 'Tesoura' or jogador == 2 and computador == 'Pedra':
        print('\033[32mVocê ganhou!\033[m')
        jogo += 1
        placar_jogador += 1
    elif jogador == 3 and computador == 'Pedra' or jogador == 2 and computador == 'Tesoura' or jogador == 1 and computador == 'Papel':
        print('\033[31mVocê perdeu!\033[m')
        jogo += 1
        placar_computador += 1
    if placar_jogador == 3:
        print(f'Você venceu a partida por \033[34m{placar_jogador}\033[m a \033[35m{placar_computador}\033[m!')
        jogo = 5
    elif placar_computador == 3:
        print(f'Você perdeu a partida por \033[35m{placar_computador}\033[m a \033[34m{placar_jogador}\033[m!')
        jogo = 5
    