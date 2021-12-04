from os import read

def read_input_from_file(filename):
    inputs = []
    input_file = open(filename, 'r')
    lines = input_file.readlines()
    for line in lines:
        inputs.append(line.strip())
    return inputs  
# algorithm
# 1. mark the drawn number in each board
# 2. if five in a row exists in a board then return the sum of all unmarked numbers 
# 3. return the last number drawn
def play_bingo(board, numbers):
    marked_matrix = [[0 for j in range(5)] for i in range(5)]
    counter = 0
    for number in numbers:
        for i in range(0,5):
            for j in range(0,5):
                if board[i][j] == number:
                    marked_matrix[i][j] = 1
        if counter >= 5:
            if check_for_bingo(marked_matrix):
                return number, sum_unmarked(board, marked_matrix), counter
        counter += 1
    return 0, 0, 0

def sum_unmarked(board, marked_matrix):
    sum = 0
    for i in range(5):
        for j in range(5):
            if marked_matrix[i][j] == 0:
                sum += board[i][j]
    return sum

def check_for_bingo(marked_matrix):
    col = 0
    for row in marked_matrix:
        if sum(row) == 5:
            return True     
        elif sum([row[col] for row in marked_matrix]) == 5:
            return True
        col += 1

def find_best_board(winning_boards):
    winning_boards.sort(key=lambda board:board[2])
    return winning_boards[0]      

def find_worst_board(winning_boards):
    winning_boards.sort(key=lambda board:board[2], reverse=True)
    return winning_boards[0]

def main():
    input_lines = read_input_from_file("in.in")
    numbers = input_lines[0].split(',')
    numbers = list(map(int, numbers))
    board = []
    board_results = []
    boards = []
    for line in input_lines[2:]:
        if line == "":
            #print(f"Board: {board}")
            result = play_bingo(board, numbers)
            if result[0] >= 0:
                #print(f"Board: {board}")
                #print(f"Numbers of numbers drawn: {result[2]}")
                #print(f"Final score: {result[0]*result[1]}")
                board_results.append(result)
            board.clear()
        else:
            board.append(list(map(int,''.join(line).split())))
    best_board = find_best_board(winning_boards=board_results)
    worst_board = find_worst_board(winning_boards=board_results)
    print(f"Best Board Attributes: {best_board}")
    print(f"Final score: {best_board[0]*best_board[1]}")
    print(f"Worst Board Attributes: {worst_board}")
    print(f"Final score: {worst_board[0]*worst_board[1]}")

    

if __name__ == '__main__':
    main()