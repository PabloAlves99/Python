import os
import time
import json

def limpar_tela():
    sistema_operacional = os.name
    if sistema_operacional == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')
  
def presentation(listTasks):   
    if listTasks:
        print('\tTarefas')
        print(*listTasks, sep='\n')
    else: 
        print('Lista de tarefas vazia')
        
def insertTask(listTasks):
    listTasks.append(input('\nQual tarefa deseja inserir? '))
    return listTasks
    
def toUndo(listTasks):
    if listTasks: 
        removeTask = listTasks.pop(-1)
        return removeTask
    else:
        print('\n\nNão existe tarefas para desfazer')
        time.sleep(2)

def remake(listTasks, removed):
    
    while len(removed) > 0:
        
        if removed[-1] == None:
            del removed[-1]
                
        elif removed:
            listTasks.append(removed.pop(-1))
            return listTasks
        
    print('\n\nNão tem oque refazer')
    time.sleep(2)
  
  
def toSave(listTasks, tasks):
    with open(tasks, 'w+', encoding='utf8' ) as tarefas:
        json.dump(listTasks, tarefas, indent=2, ensure_ascii=False)      
    
    
def command(listTasks, removed, tasks = 'tarefas.json'):

    dados = []
    if os.path.exists(tasks):
        with open (tasks, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    
    if len(dados) > 0:
        listTasks = [*dados]
    
    while True:
        limpar_tela()
        presentation(listTasks)     
        
        try:
            funcao = input('\nOpções:\n [I]nserir    [D]esfazer    [R]efazer    [C]oncluir ').upper()
            
            comandos = { # As funções só são executadas depois, quando chamadas
                'I': lambda: insertTask(listTasks),           
                'D': lambda: removed.append(toUndo(listTasks)),
                'R': lambda: remake(listTasks, removed),
                'C': lambda: toSave(listTasks, tasks)
            }    
            
            comandos.get(funcao)() # os '()' chama a execução
        except TypeError:
            print('\nDigite um dos elementos oque está entre " [] "')
            time.sleep(2)
        except:
            print('\nPara realizar alguma ação, digite apenas oque está entre " [] "')
            time.sleep(2)
            
        if funcao == 'C':
            break

if __name__ == '__main__':
    listTasks = []
    removed = []       
    command(listTasks, removed, 'tarefas.json')
            