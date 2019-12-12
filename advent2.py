import sys

input = []
with open("inputs/advent2input.txt", "r") as file:
    for line in file.readlines():
        input += line.split(",")
input = [int(x) for x in input]


def operation(type, in1, in2, target):
    if type == 1:
        input[target] = input[in1] + input[in2]
    elif type == 2:
        input[target] = input[in1] * input[in2]
    elif type == 99:
        print("Operation type 99. Halting program.")
        print("Value at position zero is: %d" % input[0])
        sys.exit()
    else:
        print("Wrong operation type!")
        sys.exit()

    print("Target value (%d): %d" %(target, input[target]))


if __name__ == '__main__':
    i = 0
    while i < len(input):
        operation(input[i], input[i + 1], input[i + 2], input[i + 3])
        i += 4
