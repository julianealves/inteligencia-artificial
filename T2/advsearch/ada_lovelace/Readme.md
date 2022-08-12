# Inteligência Artificial
Trabalho 2 da cadeira de IA (INF01048) - 2022/1

Juliane da Rocha Alves - 00285681 - Turma B  
Luiza Martins Spinelli Alves - 00326010 - Turma A  
Maria Eduarda Neves Toneto - 00323751 - Turma A  


**NOTA:** Todas as bibliotecas utilizadas no trabalho são bibliotecas nativas do Python, nenhuma biblioteca extra foi instalada.

**- Função de Avaliação:**
    A função de avaliação desenvolvida no trabalho são os pontos obtidos por uma determinada jogada, isto é, o cálculo do número de peças que determinado jogador tem no tabuleiro naquela jogada.

**- Critério de Parada:**
    O critério de parada do algoritmo é o tamanho da árvore. Foi definido que, quando a busca chega ao nível 4 da árvore, ele para. Foram realizados testes utilizando números maiores para a profundidade da busca; no entanto, mesmo obtendo resultados melhores, o tempo de execução das jogadas ultrapassava 5 segundos.

**- Melhorias:**
   Baseado no que foi explicado no tópico acima, uma das principais melhorias seria um ajuste no critério de parada. Além disso, um exemplo de melhoria que é muito utilizada junto com o minimax com poda alfa-beta é a implementação de Quiescence Search. Esse é um algoritmo normalmente utilizado para estender a busca em nós instáveis em árvores. É uma extensão da função de avaliação para adiar a avaliação até que a posição esteja estável o suficiente para ser avaliada estaticamente, ou seja, sem considerar o histórico da posição ou movimentos futuros da posição. Os "human players" geralmente possuem intuição suficiente para decidir se abandonam uma jogada que não pareça ou se buscam uma jogada promissora com grande profundidade. Esse algoritmo tenta emular esse comportamento, instruindo o computador a buscar posições "voláteis" com uma profundidade maior do que as "silenciosas" para garantir que não haja armadilhas ocultas e para obter uma estimativa melhor de seu valor. Por isso, seria uma opção que ajudaria no nosso trabalho já que poderia explorar mais possibilidades de jogadas que não venham a ser jogadas não promissoras e assim encontrar um caminho vitorioso.

**- Decisões e Dificuldades:**
    Uma dificuldade enfrentada pelo grupo durante o desenvolvimento do trabalho foi o critério de parada. Achamos que o ideal seria a busca ir mais fundo na árvore para obtermos um melhor desempenho. Entretanto, não teríamos um retorno até 5 segundos, que era um dos nossos objetivos, por isso decidimos que o limite máximo da busca seria até o nível 4. 

**- Bibliografia:**
    Material de aula sobre algoritmo minimax com poda alfa-beta.
