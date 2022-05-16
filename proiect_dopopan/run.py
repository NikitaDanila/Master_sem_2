import random
from clique import maxCliques
# maxCliques = maxCliques(0, 1)
weight_arr, value_arr = [], []
mutation_rate = 0.3
max_weight = maxCliques(0, 1)

'''(daca trece prin muchie sau nu, weight pe care-l are muchia)'''


def gen_random_populations(nr_muchii, nr_populatie):
    '''Genereaza un nr_populatii" populatii cu solutii random, fiecare cu weigth si value aleatorii'''
    all_populations = []
    for _ in range(nr_populatie):
        all_populations_arr = []
        for _ in range(nr_muchii):
            all_populations_arr.append(
                [random.randint(0, 1), round(random.uniform(0, 0.99), 2), random.randint(0, 4)])
        all_populations.append(all_populations_arr)
    # print(f'all_populations = {all_populations}')
    print('gen_random_populations')
    {print(one_pop) for one_pop in all_populations}
    print('\n')
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
        for _ in one_population:
            element_one = _[0]
            weight = _[1]
            value = _[2]
            # print(element_one, element_two)
            if(element_one == 1):
                sum_weight += weight
                sum_value += value
        weight_arr.append(sum_weight)
        if(sum_weight <= max_weight):
            one_population.append(sum_value)

        else:
            one_population.append(0)
        # print(f'new all_population = {one_population}')
    # return weight
    # print(f'weight of each population = {weight_arr}')
    # print(f'value of each population = {value_arr}')
    # print(f'new all_population = {one_population}')


def sort_populations(populations_to_generate):
    # print(f'not sorted = {populations_to_generate}')
    # # for index, tuple in enumerate(populations_to_generate):
    # #     total_value = tuple[3]
    sorted_populations = populations_to_generate.sort(reverse=True)
    print(f'sorted_populations = {sorted_populations}')


def tournament():
    pass


def crossover(genome_A, genome_B):
    '''Single Point Crossover - se alege un singur punct aleatoriu in care se face crossover-ul'''
    print('========Crossover========')
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
    print('\n\n')
    return cross_A, cross_B


def mutation(cross_A, cross_B, mutation_rate):
    print('========Mutation========')
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


populations_to_generate = gen_random_populations(4, 2)
fitness(populations_to_generate)
# print(f'populations_to_generate= {populations_to_generate}')
# sort_populations(populations_to_generate)
cross_A, cross_B = crossover(
    populations_to_generate[0], populations_to_generate[1])
mutation(cross_A, cross_B, mutation_rate)
