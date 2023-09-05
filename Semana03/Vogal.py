'''
Passo 1: Criar Dicionário para Vogal.
Passo 2: Criar um Laço For para percorrer meu texto
Passo 3: Criar um contador para as Vogais.
Passo 4: Retornar a minha função Main().
'''
def Vowel(texto):
    Vowels = {
        'a': 0, 
        'e': 0, 
        'i': 0, 
        'o': 0, 
        'u': 0
    }
    for letter in text:
        #print(letra)
        if letter in Vowels:
            Vowels[letter] += 1
    return Vowels

'''
Passo 1: Criar um Parametro para minha função.
Passo 2: Chamar a Função Vowel
'''
def main():
    text = input("Digite seu Texto: ")
    counter = Vowel(text)
    print(counter)
