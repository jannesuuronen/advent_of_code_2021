def read_input_from_file(filename):
    return list(map(int, open(file=filename, mode='r').read().split(',')))
        
def get_abs_diff(current, target):
    return abs(current-target)

def main():
    crabs = read_input_from_file("input.in")
    crabs.sort()
    total_costs = []
    for i in range(crabs[0], crabs[-1]):
        total_costs.append(sum(list(map(lambda crab, target=i: get_abs_diff(crab, target), crabs))))
    total_costs.sort()
    print(f"Total costs: {total_costs[0]}")

if __name__ == '__main__':
    main()