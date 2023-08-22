#Passo 1: Criar uma Função para receber uma lista.
#Passo 2: Filtro das Listas
#Passo 3: Criar um laço '(for)' para percorrer a lista;
#Passo 4: Remanejar valores para respectivas listas
def numbers(list):
    repeat = []
    uniques = []

    for x in list:
        if x not in uniques:
            uniques.append(x)
        elif x not in repeat:
            repeat.append(x)

    return repeat, uniques #Passo 5: Devolver ao main()
#Passo 1: Criar uma Lista
#Passo 2: Enviar para a Função '(Numbers)'
#Passo 3: Receber a lista Filtrada.
#Passo 4: Mostrar listas separadas.
def main():
    my_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
    repeat, uniques = numbers(my_list)
    print("Numero Repetido: {}".format(repeat))
    print("Numero Unico: {} ".format(uniques))

main()
