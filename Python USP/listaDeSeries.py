def adicionarSerie():
    series = []
    
    while True:
        serie = input("\nDigite em ordem de preferencia as séries que você mais gosta (ou 'sair' para encerrar): ")        
        if serie.lower() == "sair":
            break       
        series.append(serie)
        
    return series

def exibirLista(series):
    if series:
        print("\nAs suas séries preferidas são: ")
        for indice, serie in enumerate(series):
            print(f"Em {indice + 1}º lugar: {serie}")
    else:
        print("\nNenhuma série foi adicionada")
    
def main():
    print("=== Bem vindo ao catálogo de séries! === ")
    
    listaSeries = adicionarSerie()
    exibirLista(listaSeries)
    
    print("\nObrigado! Fechando a lista")
    
    
if __name__ == "__main__":
    main()