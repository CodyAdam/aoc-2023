IN = open("in.txt").read().replace(" ", "").splitlines()

times = list(map(int, IN[0].split(":")[1].strip().split()))
distances = list(map(int, IN[1].split(":")[1].strip().split()))

win_tot = 1
for i in range(len(times)):
    time = times[i]
    distance = distances[i]
    win_count = 0
    for prep_time in range(time + 1):
        run_time = time - prep_time
        distance_run = prep_time * run_time

        if distance_run > distance:
            win_count += 1
    win_tot *= win_count
print(win_tot)
            

        