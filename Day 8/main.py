from functools import singledispatch
from os import read


def read_input_from_file(filename):
    return list(open(file=filename, mode='r').readlines())

def get_output_signals(signal):
    return signal.lstrip().strip().split("|")[1]

def split_output_signals(output_sig):
    return output_sig.split(" ")

def 

def main():
    signal_patterns = read_input_from_file("input.in")
    clean_output_signals = []
    output_signals = list(map(get_output_signals, signal_patterns))
    clean_output_signals = list(map(split_output_signals, output_signals))
    clean_output_signals = [x for x in list(map(split_output_signals, output_signals)) if x]
    print(f"Output signals: {output_signals}")
    
    


if __name__ == '__main__':
    main()