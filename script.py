from input import get_data
import sys


data = get_data(sys.argv[1])
data.display()
total_time = []
jobs_start = []
workstation = data.build_workstation(0)
for i in range(data.workstations):
    workstation = data.build_workstation(i)
    workstation.workload()
    total_time.append(workstation.time)
    for j in range(data.jobs):
        jobs_start.append(workstation.jobs[j].time_done)
print(max(total_time))
for i in range(data.jobs):
    print(jobs_start[i], " ", jobs_start[data.jobs + i], " ", jobs_start[2*data.jobs + i])
