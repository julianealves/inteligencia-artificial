from copy import deepcopy
import numpy as np
import random


def evaluate(individual):
    """
    Recebe um indivíduo (lista de inteiros) e retorna o número de ataques
    entre rainhas na configuração especificada pelo indivíduo.
    Por exemplo, no individuo [2,2,4,8,1,6,3,4], o número de ataques é 10.

    :param individual:list
    :return:int numero de ataques entre rainhas no individuo recebido
    """
    attacks = 0
    # Conta o numero de ataques na mesma linha
    for i in range(len(individual)):
        for j in range(i+1, len(individual)):
            if individual[i] == individual[j]:
                attacks = attacks + 1

    # Conta numero de ataques nas diagonais
    max_cols = len(individual) - 1
    max_rows = len(individual)
    min_row = 1
    min_col = 0
    # Diagonal para cima
    for i in range(len(individual)):
        if individual[i] == 8 or i == max_cols:
            pass
        else:
            diagonal_cima = (individual[i] + 1, i + 1)
            for j in range(len(individual)):
                if individual[diagonal_cima[1]] == diagonal_cima[0]:
                    attacks = attacks + 1
                if diagonal_cima[0] == max_rows or diagonal_cima[1] == max_cols:
                    break
                diagonal_cima = (diagonal_cima[0]+1, diagonal_cima[1]+1)

    # Diagonal para baixo
    for i in range(len(individual)):
        if individual[i] == 1 or i == max_cols:
            pass
        else:
            diagonal_baixo = (individual[i] - 1, i + 1)
            for j in range(len(individual)):
                if individual[diagonal_baixo[1]] == diagonal_baixo[0]:
                    attacks = attacks + 1
                if diagonal_baixo[0] == min_row or diagonal_baixo[1] == max_cols:
                    break
                diagonal_baixo = (diagonal_baixo[0] - 1, diagonal_baixo[1] + 1)

    return attacks


def tournament(participants):
    """
    Recebe uma lista com vários indivíduos e retorna o melhor deles, com relação
    ao numero de conflitos
    :param participants:list - lista de individuos
    :return:list melhor individuo da lista recebida
    """
    best_evaluation = np.inf
    best_individual = None
    for p in participants:
        evaluation = evaluate(p)
        if evaluation < best_evaluation:
            best_evaluation = evaluation
            best_individual = p

    return best_individual


def crossover(parent1, parent2, index):
    """
    Realiza o crossover de um ponto: recebe dois indivíduos e o ponto de
    cruzamento (indice) a partir do qual os genes serão trocados. Retorna os
    dois indivíduos com o material genético trocado.
    Por exemplo, a chamada: crossover([2,4,7,4,8,5,5,2], [3,2,7,5,2,4,1,1], 3)
    deve retornar [2,4,7,5,2,4,1,1], [3,2,7,4,8,5,5,2].
    A ordem dos dois indivíduos retornados não é importante
    (o retorno [3,2,7,4,8,5,5,2], [2,4,7,5,2,4,1,1] também está correto).
    :param parent1:list
    :param parent2:list
    :param index:int
    :return:list,list
    """

    parent1_copy = deepcopy(parent1)
    parent2_copy = deepcopy(parent2)
    
    i = index 
    while i < len(parent1):
        parent1_copy[i] = parent2[i]
        parent2_copy[i] = parent1[i]
        i += 1

    return parent1_copy, parent2_copy


def mutate(individual, m):
    """
    Recebe um indivíduo e a probabilidade de mutação (m).
    Caso random() < m, sorteia uma posição aleatória do indivíduo e
    coloca nela um número aleatório entre 1 e 8 (inclusive).
    :param individual:list
    :param m:int - probabilidade de mutacao
    :return:list - individuo apos mutacao (ou intacto, caso a prob. de mutacao nao seja satisfeita)
    """
    random_number = random.random()
    print(random_number)
    if (random_number < m):
       position = random.randrange(0,7)
       number = random.randrange(1,9)
       individual[position] = number
       
       return individual
    
def create_population(n):
    """
    Cria n indivíduos aleatórios para formar uma população
    :param n: int - numero de individuos
    """
    population = []
    for i in range(n):
        individual = []
        for j in range(8):
            number = random.randrange(1,9)
            individual.append(number)
        population.append(individual)
    
    return population
    
def select_individuals(population, k):
    """
    Seleciona k individuos aleatórios de uma população
    :param population: list - lista de indivíduos (população)
    :param k: int - numero de individuos
    :return: list - lista de indivíduos (população)
    """    
    population_copy = deepcopy(population)
    new_population = []
    for i in range(k):
        position = random.randrange(len(population) - 1)
        new_population.append(population_copy[position])
        del population_copy[position]
    
    return new_population


def run_ga(g, n, k, m, e):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:int - número de indivíduos no elitismo
    :return:list - melhor individuo encontrado
    """
    p1 = None
    p2 = None
    f1 = None
    f2 = None
    best_individual = None
    
    population = create_population(n)
    for i in range(g):
        population_copy = deepcopy(population)
        new_population=[]
        for j in range(e):
            individual = tournament(population_copy)
            population_copy.remove(individual)
            new_population.append(individual)
        while len(new_population) < n:
            population = select_individuals(population, k)
            p1 = tournament(population) 
            population.remove(p1)
            p2 = tournament(population)
            population.append(p1)
            f1, f2 = crossover(p1, p2, 3)
            f1 = mutate(f1, m)
            f2 = mutate(f2, m)
            new_population.append(f1)
            new_population.append(f2)            
        population = deepcopy(new_population)    
        best_individual = tournament(population)
    return best_individual 


if __name__=="__main__":
    individual = [2, 2, 4, 8, 1, 6, 3, 4]
    print(f"Numero de ataques: {evaluate(individual)}")

    individual = [2, 7, 4, 8, 1, 6, 3, 4]
    print(f"Numero de ataques: {evaluate(individual)}")

    individual = [2, 2, 2, 2, 2, 2, 2, 2]
    print(f"Numero de ataques: {evaluate(individual)}")
