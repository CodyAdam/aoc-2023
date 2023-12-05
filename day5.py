IN = open("in.txt").read().split("\n\n")

start = list(map(int, IN[0].split(": ")[1].split()))
start_ranges = [(start[i], start[i]+start[i+1]) for i in range(0, len(start), 2)]

def parseInputToMapper(maps):
    lines = maps.split("\n")[1:]
    ranges = {}
    for line in lines:
        a, b, length = map(int, line.split())
        ranges[(b, b+length)] = a-b
    return ranges


maps = list(map(parseInputToMapper, IN[1:]))

def newRange(r: (int, int), mapper: dict[(int, int), int]):
    # low is inclusive, high is exclusive
    low, high = r
    if low > high:
        return []
    for m in mapper:
        m_low, m_high, offset = m[0], m[1], mapper[m]
        if m_low <= low and m_high >= high:
            return [(low+offset, high+offset)]
        elif m_low <= low and m_high > low:
            return [(low+offset, m_high+offset)] + newRange((m_high, high), mapper)
        elif m_low < high and m_high >= high:
            return [(m_low+offset, high+offset)] + newRange((low, m_low), mapper)
        elif m_low >= low and m_high <= high:
            return [(m_low+offset, m_high+offset)] + newRange((low, m_low), mapper) + newRange((m_high, high), mapper)
    return [r]

end_ranges = []
for start_range in start_ranges:
    current = [start_range]
    print(start_range)
    for m in maps:
        new = []
        for r in current:
            new += newRange(r, m)
        current = new
    end_ranges += current


# get min of all ranges
min_range = min(end_ranges, key=lambda x: x[0])
print("Mini : ", min_range[0])

