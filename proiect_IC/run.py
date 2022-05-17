import itertools
from multiprocessing.dummy import Array
from queue import Empty
import random
from clique import maxCliques
# maxCliques = maxCliques(0, 1)
weight_arr, value_arr, new_populations, all_populations = [], [], [], []
mutation_rate = 0.3
max_weight = maxCliques(0, 1)
generations = 100
'''(daca trece prin muchie sau nu, weight pe care-l are muchia)'''


def gen_random_populations(nr_muchii, nr_populatie) -> Array:
    '''Genereaza un nr_populatii" populatii cu solutii random, 
        fiecare cu weigth si value aleatorii
    '''
    for _ in range(nr_populatie):
        all_populations_arr = []
        for _ in range(nr_muchii):
            all_populations_arr.append(
                [random.randint(0, 1), round(random.uniform(0, 0.99), 2), random.randint(0, 4)])
        # all_populations_arr.append(0)
        all_populations.append(all_populations_arr)
    print(f'Population 0: {all_populations}\n')

    return all_populations


def fitness(all_populations):
    '''Aduna si verifica weight-ul si valoarea la fiecare populatie, daca weight-ul este mai mare decat pragul nostru
        valoarea populatiei devine 0
    '''
    print("\n========Fitness========\n")
    for one_population in all_populations:
        sum_weight = 0
        sum_value = 0
        for one_pop in one_population[:-1]:
            if(one_pop[0] == 1):
                sum_weight += one_pop[1]
                sum_value += one_pop[2]
        weight_arr.append(sum_weight)
        if(sum_weight <= max_weight):
            one_population[-1] = sum_value
        else:
            one_population[-1] = 0
        print(f'Value of population: {sum_value}')


def sort_populations(all_populations):
    for x,y in itertools.combinations(all_populations[:-1],2):
        if(x[-1] < y[-1]):
            all_populations[all_populations.index(x)], all_populations[all_populations.index(y)] = all_populations[all_populations.index(y)], all_populations[all_populations.index(x)]


def tournament():
    pass


def crossover(genome_A, genome_B):
    '''Single Point Crossover - se alege un singur punct aleatoriu in care se face crossover-ul'''
    print('\n========Crossover========\n')
    print(f'genome_A = {genome_A}\ngenome_B = {genome_B}\n\n')
    genome_length = len(genome_A)
    value_A = genome_A[-1]
    value_B = genome_B[-1]
    if genome_length < 2:
        return genome_A, genome_B

    p = random.randint(1, genome_length - 1)
    cross_A = [genome_A[0]] + genome_A[1:p] + genome_B[p:genome_length - 1]
    cross_B = [genome_B[0]] + genome_B[1:p] + genome_A[p:genome_length - 1]
    cross_A.append(value_A)
    cross_B.append(value_B)
    print(f'A_modif = {cross_A}\nB_modif =  {cross_B}')
    # print('\n\n')
    return cross_A, cross_B


def mutation(cross_A, cross_B, mutation_rate):
    print('\n========Mutation========\n')
    print(f'cross_A = {cross_A}')
    print(f'cross_B = {cross_B}\n')
    for one_genome in cross_A[:-1]:
        if random.uniform(0, 1) < mutation_rate:
            one_genome[0] = abs(one_genome[0] - 1)
    for one_genome in cross_B[:-1]:
        if random.uniform(0, 1) < mutation_rate:
            one_genome[0] = abs(one_genome[0] - 1)
    print(f'mutation_A = {cross_A}')
    print(f'mutation_B = {cross_B}')
    print('\n\n')
    all_populations[0] = cross_A
    all_populations[1] = cross_B
    print(f'all_populations = {all_populations}\n')
    return cross_A, cross_B


def run_generations(population):
    for i, _ in zip(range(generations), range(generations)):
        print(
            f'===========================GENERATION {i}========================================')
        fitness(population)
        sort_populations(population)
        cross_A, cross_B = crossover(
            population[0], population[1])
        mutation(cross_A, cross_B, mutation_rate)


populations_to_generate = gen_random_populations(6, 3)
run_generations(populations_to_generate)
