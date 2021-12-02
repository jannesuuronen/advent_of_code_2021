def read_input_from_file(filename):
    inputs = []
    input_file = open(filename, 'r')
    lines = input_file.readlines()
    for line in lines:
        inputs.append(line.strip())
    return inputs  

def calc_depth_and_horizontal_pos(instructions):
    horizontal = 0
    depth = 0
    for instruction in instructions:
        op, val = instruction.split(' ')
        val = int(val)
        if (op == "forward"):
            horizontal += val
        elif (op == "up"):
            depth -= val
        else:
            depth += val
    return horizontal, depth

def calc_depth_horizontal_pos_w_aim(instructions):
    horizontal = 0
    depth = 0
    aim = 0
    for instruction in instructions:
        op, val = instruction.split(' ')
        val = int(val)
        if (op == "forward"):
            horizontal += val
            depth += (val * aim)
        elif (op == "up"):
            aim -= val
        else:
            aim += val
    return horizontal, depth


def main():
    instructions = read_input_from_file("in.in")
    horizontal, depth = calc_depth_and_horizontal_pos(instructions)
    print(f"Product part 1: {horizontal*depth}")
    horizontal, depth = calc_depth_horizontal_pos_w_aim(instructions)
    print(f"Product part 2: {horizontal*depth}")

if __name__ == "__main__":
    main()