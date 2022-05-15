import random
from shutil import which
from clique import maxCliques
maxCliques = maxCliques(0, 1)
weight = []


def gen_random_populations(nr_muchii, nr_populatie):
    all_populations = []
    for _ in range(nr_populatie):
        all_populations_arr = []
        for _ in range(nr_muchii):
            all_populations_arr.append(
                (random.randint(0, 1), round(random.uniform(0, 0.99), 2)))
        all_populations.append(all_populations_arr)
    # print(all_populations)
    return all_populations


population = gen_random_populations(6, 3)


def fitness(one_population):
    print("fitness")
    sum = 0
    print(one_population)
    for index, tuple in enumerate(one_population):
        element_one = tuple[0]
        element_two = tuple[1]
        print(element_one, element_two)
        if(element_one == 1):
            sum += element_two
    weight.append([sum, one_population])
    return weight


def foo(fitness_func):
    solved = 0
    if fitness_func[0] == maxCliques:
        solved = 99999
    else:
        solved = abs(1 / (0.1 + fitness_func[0]))
    return [solved, fitness_func]


def func(all_populations):
    i = 0
    for one_population in all_populations:
        i += 1
        # if e clica else return gd = 0
        print("sum of weights")
        fitness_func = fitness(one_population)
        print("real")
        for iter in fitness_func:
            foo_res = foo(iter)
            print(foo_res)


def tournament():
    pass


def crossover():
    pass


def mutation():
    pass


func(population)
# GD = 6


# def foo(x, y, z):
#     return x + y + z - GD


# def fitness(x, y, z):
#     ans = foo(x, y, z)

#     if ans == GD:
#         return 99999
#     else:
#         return abs(1 / ans)


# best_found_solution = (0, 0, 0)
# rank = 0
# # generare de solutii
# solutions = []
# for s in range(1000):
#     solutions.append((random.uniform(0, 10000),
#                       random.uniform(0, 10000),
#                       random.uniform(0, 10000)))

# for i in range(10000):
#     ranked_solutions = []
#     for s in solutions:
#         ranked_solutions.append((fitness(s[0], s[1], s[2]), s))
#     ranked_solutions.sort(reverse=True)
#     print(f'=== Gen. {i} best solutions === ')
#     print(ranked_solutions[0])

#     if ranked_solutions[0][0] > 999:
#         rank, best_found_solution = ranked_solutions[0]
#         break

#     best_solutions = ranked_solutions[:100]
#     elements = []

#     for s in best_solutions:
#         elements.append(s[1][0])
#         elements.append(s[1][1])
#         elements.append(s[1][2])

#     new_gen = []
#     for _ in range(1000):
#         e1 = random.choice(elements) * random.uniform(0.99, 1.01)
#         e2 = random.choice(elements) * random.uniform(0.99, 1.01)
#         e3 = random.choice(elements) * random.uniform(0.99, 1.01)

#         new_gen.append((e1, e2, e3))

#     solutions = new_gen

# print("")
# print(rank)
# print(best_found_solution)

# question_list = []

# for test_questions in best_found_solution:
#     matching_questions = []
#     for q in questions:
#         if q.weight == round(best_found_solution[0]):
#             matching_questions.append(q)
#     question_list.append(random.choice(matching_questions))

# test_sum = 0
# for q in question_list:
#     print(q.text, end="\n")
#     for answers in q.answers:
#         print(answers)
#     user_answer = input("Raspuns:")
#     if user_answer == q.right_answer:
#         print("Corect!")
#         test_sum = test_sum + 1
#     else:
#         print(f'Gresit! Raspunsul corect era {q.right_answer}')

# print(f"Felicitari! Ai reusit sa raspunzi corect la {test_sum} intrebari!")
