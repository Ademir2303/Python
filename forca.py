#importar random para randomizar as palavras
import random
from os import system, name
#função para limpar a tela em cada execução no windows
def limpar():
    if name == "nt":
        _=system("cls")

#função
def game():
    limpar()

    print("\n Bem vindo(a) ao jogo da forca")
    print("\n Adivinhe a palavra abaixo:\n")

    #Lista de palavras para a forca
    palavras = ['mandioca','batata','morango']

    #Escolhe de forma randomizada
    palavra = random.choice(palavras)

    #lista para demostrar letras descobertas
    letras_descobertas = ['_' for letra in palavra]
    
    #tentativas restantes
    chances = 10

    #lista para qnt de erros
    letras_erradas = []

    #loop enquanto numero de chances for maior do que zero
    while chances> 0 :
        print(" ".join(letras_descobertas))
        print(f"\nChances restantes:", chances)
        print(f"Letras erradas:\n" " ".join(letras_erradas))

        #tentativas
        tentativa = input('\nDigite uma letra: ').lower()

        #condicional
        if tentativa in palavra:
             for index, letra in enumerate(palavra):
                if tentativa == letra:
                    letras_descobertas[index] = letra
        else:
            chances -= 1
            letras_erradas.append(tentativa)
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break
    
    #condicional
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra)

#bloco main
if __name__ == "__main__":
    game()
