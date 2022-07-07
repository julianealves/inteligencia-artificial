from nodo import Nodo
from sucessor import sucessor

# Exemplos para testar:
nodo_pai = Nodo(estado="2_3541687")
nodo_filho1 = Nodo(estado="_23541687", pai=nodo_pai, acao="esquerda")
nodo_filho2 = Nodo(estado="2435_1687", pai=nodo_pai, acao="abaixo")
nodo_filho3 = Nodo(estado="23_541687", pai=nodo_pai, acao="direita")


def expande(nodo):
    
    listOfNodes = []
    listOfSucc = sucessor(nodo.estado)     
         
    for acao, estado in listOfSucc:
        nodoSucc = Nodo(estado=estado, pai=nodo, acao=acao)
        listOfNodes.append(nodoSucc)        
   
    return listOfNodes


def main():
    sucessores = expande(nodo_pai)
    
    for nodo in sucessores:
         print(nodo.estado, nodo.pai, nodo.acao, Nodo.get_custo(nodo))    #Fiquei com duvida como que é para referenciar o nodo.pai nessa função

    return 0


if __name__ == "__main__":
    main()
    
    
    
    
    
    
