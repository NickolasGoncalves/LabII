'''
Passo 1: Criar uma Lista
Passo 2: Criar uma Variavel para verificar uma Key
Passo 3: True/False para o nome verificado
'''
def main():
    key = {
        'Maça' : 'Maça',
        'Melancia' : 'Melancia',
        'Melão' : 'Melão'
        }
    a = input("Digite uma Palavra: ")

    if a in key:
        print(bool(True))
    else:
        print(bool(False))

main()
