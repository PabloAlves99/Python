import os
import time

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
        
def insertTask(list):
    list.append(input('\nQual tarefa deseja inserir? '))
    return listTasks
    
def toUndo(list):
    removeTask = list.pop(-1)
    return removeTask

def remake(list, removed):
    if removed:
        list.append(removed.pop(-1))
        return list
    else:
        print('\n\nNão tem oque refazer')
        time.sleep(2)
    
def command(listTasks, removed):
    
    while True:
        limpar_tela()
        presentation(listTasks)     
        
        funcao = input('\nOpções:\n [I]nserir    [D]esfazer    [R]efazer    [C]oncluir ').upper()
            
        if funcao == ('I' or 'INSERIR'): # Inserir tarefa
            insertTask(listTasks)
            
        elif funcao == ('D' or 'DESFAZER'): # Remover ultima tarefa
            if listTasks:
                removed.append(toUndo(listTasks))
            else:
                print('\n\nNão existe tarefas para desfazer')
                time.sleep(2)
            
        elif funcao == ('R' or 'REFAZER'): # Adicionar novamente tarefas removidas
            remake(listTasks, removed)
            
        elif funcao == ('C' or 'CONCLUIR'): # Parar o while infinito
            return list
        else:
            print('\n\nDigite apenas uma das opções válida\n\n')
            time.sleep(2)

if __name__ == '__main__':
    listTasks = []
    removed = []       
    command(listTasks, removed)
            