import random
from os import system

#cls e clear para limpar o terminal
def game():
    system('cls||clear')
    print("\n Jogo da Forca - Adivinhe a palavra:\n")
    
    palavra = random.choice(['mandioca', 'batata', 'morango', 'abacaxi', 'chocolate'])
    descobertas = ['_'] * len(palavra)
    erradas, chances = [], 7

    #loop para demonstrar as letras descobertas, chances e erradas

    while chances > 0 and '_' in descobertas:
        print(f"{' '.join(descobertas)} | Chances: {chances} | Erros: {' '.join(erradas)}")
        tentativa = input('\nLetra: ').lower().strip()

        #para vereficar se a palavra existe na run atual

        if tentativa in palavra:
            for i, letra in enumerate(palavra):
                if letra == tentativa: descobertas[i] = letra
            print(" Acertou!")
        else:
            chances -= 1
            erradas.append(tentativa)
            print(" Errou!")
    
    print(f"\n{' Você VENCEU!' if '_' not in descobertas else ' Você PERDEU!'}")
    print(f"Palavra: {palavra.upper()}")

if __name__ == "__main__":
    game()
