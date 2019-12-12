def calc_fuel(mass):
    fuel = int(mass / 3) - 2
    if fuel < 0:
        fuel = 0
    else:
        fuel += calc_fuel(fuel)
    return fuel


if __name__ == '__main__':

    fuel = 0

    with open("inputs/advent1input.txt") as file:
        line = file.readline()
        cnt = 0
        while line:
            fuel += calc_fuel(int(line))
            line = file.readline()
            cnt += 1

    print("Number of inputs: %d" % cnt)
    print("Needed fuel for launch: %d" % fuel)
