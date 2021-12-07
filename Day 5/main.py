def is_hori_vert_line(line):
    return line[0][0] == line[1][0] or line[0][1] == line[1][1]

# algorithm
# 1. 

def read_input_from_file(filename):
    inputs = []
    input_file = open(filename, 'r')
    lines = input_file.readlines()
    for line in lines:
        inputs.append(line.strip().replace('->',''))
    return inputs  

def main():
    lines = []
    inputs = read_input_from_file("in.in")
    for input in inputs:
        pairs = input.split()
        start, end = tuple(map(int, pairs[0].split(","))), tuple(map(int, pairs[1].split(",")))
        lines.append((start, end))
    
    lines = list(filter(is_hori_vert_line, lines))
    print(f"Number of lines:{len(lines)}")
    
    num_inter = 0
    offset = 0
    for line_a in lines:
        offset += 1
        for line_b in lines[offset:]:
            num_inter += check_for_intersection(line_a, line_b)

    print(f"Number of intersections: {num_inter}")
    

    


if __name__ == '__main__':
    main()