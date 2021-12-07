from os import rename
import multiprocessing as mp

def read_input_from_file(filename):
    return list(map(int, open(file=filename, mode='r').read().split(',')))

def decrement(number):
    return number - 1

def reset(number):
    if number == -1:
        return 6
    return number      

def grow_population(population):
    population = [population]
    for i in range(256):
        population = list(map(decrement, population))
        num_birthing = population.count(-1)
        population = list(map(reset, population))
        population.extend([8 for j in range(num_birthing)])
    return len(population)

def main():
    print(f"Number of processors: {mp.cpu_count()}")
    pool = mp.Pool(mp.cpu_count())
    population = read_input_from_file("input.in")
    # pre-allocate bins
    pops = [[] for i in range(len(population))]
    for pop in pops:
        pop.append(population.pop(0))
    num_days = 256
    res = list(map(lambda x: pool.map(grow_population, x), pops))
    mp.freeze_support()
    print(f"Result: {res}")
    # algorithm 1:
    # age population by one day
    # reset all fish that are -1 days old
    # if fishes are -1 day old then append new fishes equal to the number of fishes -1 days old
    # for i in range(num_days):
    #     population = list(map(decrement, population))
    #     num_birthing = population.count(-1)
    #     population = list(map(reset, population))
    #     population.extend([8 for j in range(num_birthing)])

    # algorithm 2:
    # split initial population into bins
    # age each sub population by one day
    # reset all fish in each sub population that are -1 days old
    # if fishes are -1 day old then append new fishes equal to the number of fishes -1 days old

    # flatten populations
    #flatten_pops = [fish for subpop in res for fish in subpop]



if __name__ == '__main__':
    main()