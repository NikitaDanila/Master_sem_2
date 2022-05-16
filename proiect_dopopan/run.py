import random
from clique import maxCliques
# maxCliques = maxCliques(0, 1)
weight_arr, value_arr = [], []
mutation_probability = 0.5
max_weight = maxCliques(0, 1)

'''(daca trece prin muchie sau nu, weight pe care-l are muchia)'''


def gen_random_populations(nr_muchii, nr_populatie):
    '''Genereaza un nr_populatii" populatii cu solutii random, fiecare cu weigth si value aleatorii'''
    all_populations = []
    for _ in range(nr_populatie):
        all_populations_arr = []
        for _ in range(nr_muchii):
            all_populations_arr.append(
                (random.randint(0, 1), round(random.uniform(0, 0.99), 2), random.randint(0, 4),0))
        all_populations.append(all_populations_arr)
    # print(f'all_populations = {all_populations}')
    return all_populations


def fitness(all_populations):
    '''Aduna si verifica weight-ul si valoarea la fiecare populatie, daca weight-ul este mai mare decat pragul nostru
        valoarea populatiei devine 0
    '''
    # print("fitness")
    sum_weight = 0
    sum_value = 0
    # print(f'one_population = {one_population}')
    for one_population in all_populations:
        sum_weight = 0
        sum_value = 0
        for index, tuple in enumerate(one_population):
            element_one = tuple[0]
            weight = tuple[1]
            value = tuple[2]
            total_value = tuple[3]
            # print(element_one, element_two)
            if(element_one == 1):
                sum_weight += weight
                sum_value += value
        weight_arr.append(sum_weight)
        if(sum_weight <= max_weight):
            # value_arr.append(sum_value)
            total_value = sum_value
        else:
            # value_arr.append(0)
            total_value = 0
    # return weight
    # print(f'weight of each population = {weight_arr}')
    # print(f'value of each population = {value_arr}')


def sort_populations(populations_to_generate):
    print(f'not sorted = {populations_to_generate}')
    # for index, tuple in enumerate(populations_to_generate):
    #     total_value = tuple[3]
    sorted_populations = populations_to_generate.sort(key=tuple[3], reverse=True)
    print(f'sorted_populations = {sorted_populations}')

def tournament():
    pass


def crossover(genome_A, genome_B):
    '''Single Point Crossover - se alege un singur punct aleatoriu in care se face crossover-ul'''
    print(f'genome_A = {genome_A}\ngenome_B = {genome_B}\n\n')
    genome_length = len(genome_A)
    if genome_length < 2:
        return genome_A, genome_B

    p = random.randint(1, genome_length - 1)
    cross_A = genome_A[0:p] + genome_B[p:]
    cross_B = genome_B[0:p] + genome_A[p:]
    print(f'A_modif = {cross_A}\nB_modif =  {cross_B}')

    return cross_A, cross_B


def mutation():
    pass


populations_to_generate = gen_random_populations(6, 8)
fitness(populations_to_generate)
sort_populations(populations_to_generate)
# cross_A, cross_B = crossover(populations_to_generate[0], populations_to_generate[1])
# mutation(cross_A, cross_B)
