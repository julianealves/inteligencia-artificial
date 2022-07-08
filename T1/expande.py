from T1.nodo import Nodo
from T1.sucessor import sucessor
from typing import List


def expande(nodo: Nodo) -> List:
    """
    Metodo recebe um nodo e retorna uma lista com todos os nodos sucessores a este

    :param nodo: Recebe o nodo a ser expandido
    :return: Lista com os nodos sucessores
    """
    
    listOfNodes = []
    listOfSucc = sucessor(nodo.estado)     
         
    for acao, estado in listOfSucc:
        nodoSucc = Nodo(estado=estado, pai=nodo, acao=acao)
        listOfNodes.append(nodoSucc)        
   
    return listOfNodes
