import fileinput
from input import get_data
import sys


data = get_data(sys.argv[1])
input = fileinput.input(sys.argv[2])
time = int(input[0])
t = []
for line in input:
    line_numbers = [int(jobs) for jobs in line.split()]
    t.append(line_numbers)
workstations = len(t[0])
print("workstations number = ", workstations)

times = []
for ws in range(workstations):
    for item in t:
        times.append(item[ws])
    now = 0
    done_time = []
    print("WORKSTATION ", ws)
    for i in range(len(times)):
        if now not in times:
            print("FUCK IT in", i)
            # sys.exit()
        else:
            print("time is ", now)
            running = times.index(now)
            print("running job ", running)
            x = data.matrix[running][ws + 1]
            now = x + now
            print("#####")
    done_time.append(now)
    times.clear()


if max(done_time) == time:
    print("verified")
