import random
'''
Passo 1: Criar uma Função para gerar numeros aleatorios.
Passo 2: Lista Para o Bingo
Passo 3: Lista para os numeros
Passo 4: Verificar se existe numeros repetidos
Passo 5: Retornar a cartela para Main()
'''
def numero():
    bingo = []
    values = []

    for line in range(5):
        bingo.append([])
        num = random.randint(0, 99)

        while num in values:
            num = random.randint(0, 99)

        if num not in values:
            bingo[line].append(num)
            values.append(num)
    
    return bingo

def main():
    bingo = numero()
    print(bingo)


main()
