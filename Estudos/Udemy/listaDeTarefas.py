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
  
  
def toSave(listTasks):
    with open('tarefas.json', 'w+', encoding='utf8' ) as tarefas:
        dados = json.dump(listTasks, tarefas, indent=2, ensure_ascii=False)
        
    
    
def command(listTasks, removed):
    
    dados = []
    with open ('tarefas.json', 'r', encoding='utf8') as arquivo:
        dados = json.load(arquivo)
        
    if len(dados) > 0:
        listTasks = [*dados]
    
    while True:
        limpar_tela()
        presentation(listTasks)     
          
        try:
            funcao = input('\nOpções:\n [I]nserir    [D]esfazer    [R]efazer    [C]oncluir ').upper() #Falta implementar o C
            
            comandos = { # As funções só são executadas depois, quando chamadas
                'I': lambda: insertTask(listTasks),           
                'D': lambda: removed.append(toUndo(listTasks)),
                'R': lambda: remake(listTasks, removed),
                'C': lambda: toSave(listTasks)
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

            # PARA EXECUTAR ESSE CÓDIGO VAI PRECISAR DE ALTERAR AS FUNCOES
        # if funcao == ('I' or 'INSERIR'): # Inserir tarefa
        #     insertTask(listTasks)
            
        # elif funcao == ('D' or 'DESFAZER'): # Remover ultima tarefa
        #     if listTasks:
        #         removed.append(toUndo(listTasks))
        #     else:
        #         print('\n\nNão existe tarefas para desfazer')
        #         time.sleep(2)
            
        # elif funcao == ('R' or 'REFAZER'): # Adicionar novamente tarefas removidas
        #     remake(listTasks, removed)
            
        # elif funcao == ('C' or 'CONCLUIR'): # Parar o while infinito
        #     return listTasks
        # else:
        #     print('\n\nDigite apenas uma das opções válida\n\n')
        #     time.sleep(2)

if __name__ == '__main__':
    listTasks = []
    removed = []       
    command(listTasks, removed)
            