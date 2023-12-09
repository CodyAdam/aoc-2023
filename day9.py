IN = open("in.txt").read().splitlines()


def get_next(arr):
    return [arr[i+1]-arr[i] for i in range(len(arr)-1)]


def is_all_zero(arr):
    for i in arr:
        if i != 0:
            return False
    return True

s = 0
for line in IN:
    values = list(map(int, line.split(" ")))
    layers = [values]
    while not is_all_zero(layers[-1]):
        layers.append(get_next(layers[-1]))

    for i in range(len(layers)-2, -1, -1):
        layers[i].insert(0, layers[i][0]-layers[i+1][0])
    s += layers[0][0]
    print(line, layers[0][0])
print(s)
