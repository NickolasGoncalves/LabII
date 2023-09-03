'''
Passo 1: Criar um dicionário Vazio
Passo 2: Passar o parametro para função Dias
Passo 3: Atribuir ao meu dicionário Chaves e valores
Passo 4: Percorrer meu Dicionário
Passo 5: Retornar ao Main

'''
def day(days):
    day = {}
    day['Domingo'] = ['Sem Aula']
    day['Segunda']= ['Sem Aula']
    day['Terça'] = ['Laborátorio de Algoritmo II']
    day['Quarta'] = ['Sem Aula']
    day['Quinta']= ['Probabilidade e Estatistica']
    day['sexta'] = ['Fundamentos de Economia e Administração']
    day['sabado'] = ['Sem Aula']
    
    for days, content in day.items():
        print(days, content)
    return days
    
'''
Passo 1: Puxar minha função para o Dicionário Principal
'''
def main():
    week = {}

    weeks = day(week)
    
main()
