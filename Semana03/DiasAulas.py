'''
Passo 1: Criar um dicionário Vazio
Passo 2: Passar o parametro para função Dias
Passo 3: Atribuir ao meu dicionário Chaves e valores
Passo 4: Percorrer meu Dicionário
Passo 5: Retornar ao Main

'''
def day(days):
    day = {
    'Domingo',
    'Segunda',
    'Terça',
    'Quarta',
    'Quinta', 
    'sexta', 
    'sabado'
    }
    for day in week_days:
        class_day = input(f"Qual aula você têm na(o) {day}")
        week[day] = class_day
    
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
