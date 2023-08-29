import random

lista_de_palavras = ["Banana", "Maca", "Abacaxi", "Laranja", "Uva", "Manga", "Abobora", "Cenoura", "Alface", "Brocolis",
            "Tomate", "Batata", "Pera", "Melancia", "Morango", "Kiwi", "Espinafre", "Cebola", "Pepino", "Limao"]

board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<
+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class Hangman:
    def __init__(self):
        self.palavra_escolhida = random.choice(lista_de_palavras).lower()
        self.palavra_escolhida_not_repeated = "".join(set(self.palavra_escolhida))
        self.caracteres_validos = []
        self.caracteres_invalidos = []

    def set_attempt(self):
        print((board[len(self.caracteres_invalidos)]))
        print('\nLetras Corretas => ', self.caracteres_validos)
        print("\nLetras Erradas => ", self.caracteres_invalidos, '\n')
        tentativa = input("Escreva a letra desejada\n ")
        if len(tentativa) > 1:
            print("Jogada Inválida")
            return
        elif tentativa in self.caracteres_invalidos:
            print("Letra Repetida =(")
        elif tentativa in self.caracteres_validos:
            print("Letra já foi usada =(")
        else:
            if tentativa in self.palavra_escolhida:
                self.caracteres_validos.append(tentativa)
                print("Caractere Válido")
            else:
                self.caracteres_invalidos.append(tentativa)
                print("Caractere Inválido")
                print(board[len(self.caracteres_invalidos)])
        if len(self.caracteres_invalidos) == 6:
            print("Gamer Over")
            return True
        if len(self.caracteres_validos) == len(self.palavra_escolhida_not_repeated):
            print("Ganhou o jogo")
            return True
        
    def reveal_word(self):
        word_replaced = []
        for letra in self.palavra_escolhida:
            if letra in self.caracteres_validos:
                word_replaced.append(letra)
            else:
                word_replaced.append(" _ ") 
        print("\n" + "".join(word_replaced) + "\n\n")       

def main():
    hangman = Hangman()
    #print(board[0])
    hangman.reveal_word()
    
    while True:
        must_stop = hangman.set_attempt()
        hangman.reveal_word()
       
        if must_stop:
            break
        



main()


    

































