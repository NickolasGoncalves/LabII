'''
Passo 1: Criar um Dicionário Vazio para receber como parametro.
Passo 2: Atribuir Chave e Valor.
Passo 3: Percorrer meu Dicionário
Passo 4: Retornar meu dicionário preenchido ao main()
'''
def film(films):
    movie = {}
    movie['Star Wars'] = ['Darth Vader'], ['1977']
    movie['Homem de Ferro 1'] = ['Obadiah Stane'], ['2008']
    movie['Harry Potter'] = ['Voldemort'], ['2001']
    movie['Narnia'] = [' Feiticeira Branca'], ['2008']
    movie['Homem-Aranha 2'] = [' Doutor Octopus'], ['2004']

    for keys, values in movie.items():
        print(f'Nome do Filme: {keys}, {values}')
    return movie


'''
Passo 1: Criar um Dicionário Vazio.
Passo 2: Criar uma Variavel para chamar a Função com valores
'''


def main():
    movies = {}

    films = film(movies)

main()
    
    
