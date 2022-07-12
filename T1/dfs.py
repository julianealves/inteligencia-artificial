from typing import List
from nodo import Nodo
from expande import expande
from astar import caminho_s_v
import time

# Não está pronto, vou tentar arrumar amanhã, mas se tiverem alguma ideia, é muito bem vinda.

def dfs(estado: str) -> List:
    
    nodo_raiz = Nodo(estado=estado, pai=None, acao=None, custo=0)
    solucao = "12345678_"
    explorados = []
    visitados = []
    fronteira : List[Nodo] = []    

    fronteira.append(nodo_raiz)
    
    while len(fronteira) != 0:
        
        v = fronteira.pop()
        
        if v.estado == solucao:
            return caminho_s_v(v, [])        
        
        if v not in explorados:
            explorados.append(v)
            vizinhos = expande(v)  
            visitados.append(v.estado)
            for s in vizinhos:
                if s.estado not in visitados:
                    fronteira.append(s)
    
    return None
            
    
def main():
   inicio = time.time()
   n = dfs("23_541687")
   fim = time.time()
   print(f"Tempo execução: {fim - inicio}")
   print(n)

if __name__ == "__main__":
    main()           


     
