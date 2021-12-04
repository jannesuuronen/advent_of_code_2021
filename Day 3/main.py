from os import read
from collections import Counter

def get_mcb(bit_str):
    occurence_count = Counter(bit_str)
    bag = occurence_count.most_common(2)
    if bag[0] == bag[1]:
        if (bag[0] == '1'):
            return bag[0][0]
        else:
            return bag[1][0]
    
    return occurence_count.most_common(1)[0][0]


def get_most_frequent(list):
    occurence_count = Counter(list)
    bag = occurence_count.most_common(2)
    return occurence_count.most_common(1)[0]

def read_input_from_file(filename):
    inputs = []
    input_file = open(filename, 'r')
    lines = input_file.readlines()
    for line in lines:
        inputs.append(line.strip())
    return inputs  

def trans_cols_to_bin_strs(readings):
    binary_strings = []
    for i in range(len(readings[0])):
        binary_strings.append([row[i] for row in readings])
    return binary_strings

def negate_bit(bit):
    if bit == '0':
        return '1'
    else:
        return '0'    

def calc_gamma_epsilon_rates(readings):
    bin_strs = trans_cols_to_bin_strs(readings)
    gamma = []
    for str in bin_strs:
        gamma.append(get_most_frequent(str)[0])
    epsilon = list(map(negate_bit, gamma))
    print(f"Gamma: {gamma}, Epsilon: {epsilon}")
    gamma = int(' '.join(gamma).replace(' ',''), 2)
    epsilon = int(' '.join(epsilon).replace(' ',''), 2)
    return gamma, epsilon    

def get_valid_str(str, pos, val):
    if str[pos] == val:
        return str

def calc_oxygen_rate(readings):
    
    reads_matrix = [[] for i in range(len(readings))]
    solution = []
    for i in range(len(readings)):
        reads_matrix[i] = [int(bit) for bit in readings[i]]

    # bit matrix
    # find most common value in column i
    # remove rows that doesn't have the most common bit at position i
    j = 0
    for i in range(len(reads_matrix[0])-1):
        col = [row[i] for row in reads_matrix]
        print(f"Col: {col}, i: {i}")
        mcb = get_mcb(col)
        solution = [v for v in reads_matrix if v[j] == mcb]
        j += 1
    print(f"Solution: {solution}")
def calc_oxygen_co2_rates(readings):
    oxygen_rate = calc_oxygen_rate(readings)



def main():
    readings = read_input_from_file("in.in")
    gamma, epsilon = calc_gamma_epsilon_rates(readings)
    print(f"Power consumption: {gamma*epsilon}")
    calc_oxygen_co2_rates(readings=readings)

if __name__ == '__main__':
    main()