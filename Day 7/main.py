def read_input_from_file(filename):
    return list(map(int, open(file=filename, mode='r').read().split(',')))
        
def get_abs_diff(current, target):
    return abs(current-target)

# algorithm 2:
# cost = 1 + previous step
# abs(cur-target) gives us the number of steps 
# given the number of steps gives us the range 1 to steps
# 
def get_stagged_diff(current, target):
    return abs(current-target) * (abs(current-target) + 1) // 2

def main():
    crabs = read_input_from_file("input.in")
    crabs.sort()
    total_costs = []
    for i in range(crabs[0], crabs[-1]):
        total_costs.append(sum(list(map(lambda crab, target=i: get_abs_diff(crab, target), crabs))))
    total_costs.sort()
    print(f"Total costs Part 1: {total_costs[0]}")
    total_costs.clear()
    for i in range(crabs[0], crabs[-1]):
        total_costs.append(sum(list(map(lambda crab, target=i: get_stagged_diff(crab, target), crabs))))
    print(f"Total cost for Part 2: {total_costs[0]}")
if __name__ == '__main__':
    main()