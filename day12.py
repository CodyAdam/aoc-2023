from functools import cache
from itertools import combinations


IN = open("in.txt").read().splitlines()

@cache
def get_possible(length: int, count: int):
    """
    return the possible combinations of binary length `length` with `count` 1s

    >>> get_possible(3, 2)
    ['011', '101', '110']

    >>> get_possible(4, 3)
    ['0111', '1011', '1101', '1110']
    
    >>> get_possible(5, 5)
    ['11111']
    """
    indices = range(length)
    result = []
    for comb in combinations(indices, count):
        binary = ['.'] * length
        for index in comb:
            binary[index] = '#'
        result.append(''.join(binary))
    return result


def is_valid(val, nums):
    groups = val.split(".")
    groups = list(filter(lambda x: x != "", groups))
    
    try:
        for i, group in enumerate(groups):
            if len(group) != nums[i]:
                return False
    except IndexError:
        return False
    return True

s = 0
for line in IN:
    # .??..??...?##. 1,1,3
    val, right = line.split(" ")
    val = val + val + val + val + val
    nums = [int(x) for x in right.split(",")]
    nums = nums + nums + nums + nums + nums
    print(val, nums)
    intero_count = val.count("?")
    hash_count = val.count("#")

    n = sum(nums)
    poss = get_possible(intero_count, sum(nums) - hash_count)
    for p in poss:
        # print(p)
        replaced = val
        founded =0 
        for i, char in enumerate(replaced):
            if char == "?":
                replaced = replaced[:i] + p[founded] + replaced[i+1:]
                founded += 1
        if is_valid(replaced, nums):
            s += 1
print(s)
