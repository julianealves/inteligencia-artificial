# Inteligência Artificial
Trabalho 1 da cadeira de IA (INF01048) - 2022/1

Juliane da Rocha Alves - 00285681 - Turma B  
Luiza Martins Spinelli Alves - 00326010 - Turma A  
Maria Eduarda Neves Toneto - 00323751 - Turma A  


Para a entrada "2_3541687", os valores computados para cada algoritmo são:
- **Algoritmo BFS:** Nós expandidos =  109477  
                 Custo =  23  
                 Tempo execução =  1.9679319858551025 s

- **Algoritmo DFS:** Nós expandidos = 64277  
                 Custo = 55003  
                 Tempo execução = 0.5804741382598877 s  
                 
- **Algoritmo A\* Hamming:** Nós expandidos = 12251  
                        Custo = 23  
                        Tempo execução Hamming = 0.12551331520080566 s

- **Algoritmo A\* Manhattan:** Nós expandidos = 1552  
                          Custo = 23  
                          Tempo execução Manhattan = 0.09373831748962402 s
  

**NOTA:** Todas as bibliotecas utilizadas no trabalho são bibliotecas nativas do Python, não sendo necessário a instalção de bibliotecas extras.
Para executar apenas o arquivo solução, basta executar:

```
$ python solucao.py
```

Para a execução dos Unit Testes que se encontram na pasta *testes*, basta executar:
```
$ python -m unittest testes/<nome_do_arquivo>.py
```