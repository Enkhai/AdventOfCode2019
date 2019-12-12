import sys

input_list = []
with open("inputs/advent2input.txt", "r") as file:
    for line in file.readlines():
        input_list += line.split(",")
input_list = [int(x) for x in input_list]


def operation(op_type, in1, in2, target):
    if op_type == 1:
        input_list[target] = input_list[in1] + input_list[in2]
    elif op_type == 2:
        input_list[target] = input_list[in1] * input_list[in2]
    elif op_type == 99:
        print("Operation type 99. Halting program.")
        print("Value at position zero is: %d" % input_list[0])
        sys.exit()
    else:
        print("Wrong operation type!")
        sys.exit()

    print("Target value (%d): %d" % (target, input_list[target]))


if __name__ == '__main__':
    i = 0
    while i < len(input_list):
        operation(input_list[i], input_list[i + 1], input_list[i + 2], input_list[i + 3])
        i += 4
