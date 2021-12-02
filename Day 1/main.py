def read_input_from_file(filename):
    inputs = []
    input_file = open(filename, 'r')
    lines = input_file.readlines()
    for line in lines:
        inputs.append(line.strip())
    return inputs    

def get_list_chunks(measurements, win_size):
    chunk_list = list()
    for i in range(0, len(measurements), 1):
        chunk_list.append(measurements[i:i+win_size])
    return chunk_list

def get_num_increases(measurements):
    chunks = get_list_chunks(measurements, 3)
    no_increases = 0
    prev_sum = sum(chunks[0][0:3])
    for i in range(1, len(chunks)):
        meas_sum = sum(chunks[i][0:3])
        if prev_sum < meas_sum:
            no_increases += 1
        prev_sum = meas_sum
    return no_increases

def main():
    measurements = read_input_from_file("in.in")
    measurements = list(map(int, measurements))
    no_increases = 0
    for i in range(len(measurements)-1):
        if measurements[i] < measurements[i+1]:
            no_increases += 1
    print(f"Number of increases in Part 1: {no_increases}")

    no_increases = get_num_increases(measurements)
    print(f"Number of increases in Part 2: {no_increases}")

    return True

if __name__ == '__main__':
    main()