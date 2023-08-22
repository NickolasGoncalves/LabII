#Passo 1: Criar uma Função para receber uma matriz;
#Passo 2: Definir um local para receber a soma dos numeros;
#Passo 3: Definir uma lista para receber a média de somas
#Passo 4: Criar um laço '(For)' para percorrer a Matriz
#Passo 5: A cada linha somar todos os numeros;
    #Passo 5.1: Dividir a soma pela quantidade de itens na linha.
#Passo 6: Adicionar a lista;
#Passo 7: Somar toda a matriz e dividir pela quantidade de itens;

def multiplication(matriz):
    totalnum = 0
    average = []

    
    for x in matriz:
        number = sum(x)  
        averages = number / len(x)  
        totalnum += number
        average.append(averages)

    total = totalnum / (len(matriz) * len(matriz[0]))  

    return total, average #Passo 8: Devolver a função Global;

#Passo 1: Criar uma Matriz;
#Passo 2: Enviar a Matriz Global para a função Local
#Passo 3: Receber a média da Matriz
def main():
    matriz =    [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
    total, average = multiplication(matriz)
    print("Média Total: {}".format(total))
    print("Média por Linha: {}".format(average))


main()
