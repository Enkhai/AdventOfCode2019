import sys

initial_list_data = []
with open("inputs/advent2input.txt", "r") as file:
    for line in file.readlines():
        initial_list_data += line.split(",")
initial_list_data = [int(x) for x in initial_list_data]


def operation(op_code, in1, in2, target, data):
    if op_code == 1:
        data[target] = data[in1] + data[in2]
    elif op_code == 2:
        data[target] = data[in1] * data[in2]
    elif op_code == 99:
        return "exit"
    else:
        print("Wrong operation type!")
        sys.exit()

    return 0


def output(data):
    i = 0
    while i < len(data):
        if operation(data[i], data[i + 1], data[i + 2], data[i + 3], data) == "exit":
            break
        i += 4
    return data[0]


if __name__ == '__main__':
    for noun in range(100):
        for verb in range(100):

            list_data = initial_list_data.copy()
            list_data[1] = noun
            list_data[2] = verb

            if output(list_data) == 19690720:
                print(100 * noun + verb)
                sys.exit()
