from random import choice
from os import system
from colorama import init, Fore

def perdeu():
    if (contador_erros == 6):
        print(Fore.RED + '\n\nVoce perdeu 😪!!\n' + Fore.RESET)
        return True
    else:
        return False

def printa_forca():
    # Printa a forca correta
    print(Fore.CYAN)
    with open(f"sprites/sprite{contador_erros}.txt", "r") as forca:
        for i in forca:
            print(i, end="")
    print("\n" + Fore.RESET)

def mostra_chutes():
    print("\nChutes realizados: ", end="| ")
    for chute in lista_palpites:
        print(f"{chute} | ", end='')

def palpite_valido():
    if (palpite not in lista_palpites and len(palpite) == 1 and palpite.isalpha()):
        return True
    else:
        print(Fore.RED+"\nEntrada inválida 😡 | Digite 1 caractere, por favor"+Fore.RESET)
        return False

def ganhou():
    if letras_restantes == 0:
        print(Fore.CYAN + 'Voce ganhou o jogo 🥳!!'+Fore.RESET)
        return True
    
def criptografa_palavra():
    print("\nSua palavra: ", end=" ")
    numero_letras = (len(palavra_escolhida))
    for i in range (numero_letras):
        print('_', end=' ')

def errou_palpite():
    if (palpite not in palavra_escolhida):
        return True
    else:
        return False

init()

lista_palavras = []
lista_palpites = []

# Escolhe uma palavra aleatoria
with open("palavras.txt", "r") as arquivo:
    for palavra in arquivo:
        lista_palavras.append(palavra.strip()) # Limpa os caracteres em branco e as quebras de linha

palavra_escolhida = choice(lista_palavras)

criptografa_palavra()
print()

contador_erros = 0
while True:
    if (perdeu()):
        break

    palpite = input('\nDigite uma letra: ').lower()
    
    if (palpite_valido()):
        system("clear")
        lista_palpites.append(palpite)
        lista_palpites.sort()
    else:
        continue # Ao ler o continue, o laço volta pro inicio

    if (errou_palpite()):
        contador_erros += 1

    # Printa a palavra criptografada e realiza a lógica de vitória
    print()
    letras_restantes = 0
    for letra in palavra_escolhida:
        if letra in lista_palpites:
            print(letra, end = ' ')
        else:
            print('_', end = ' ')
            letras_restantes += 1
    print("\n")

    if (ganhou()):
        break

    printa_forca()
    mostra_chutes()

print('Fim de jogo, a palavra era: ' + Fore.CYAN + f'{palavra_escolhida}\n')




