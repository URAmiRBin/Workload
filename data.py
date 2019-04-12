class Data:
    def __init__(self, jobs, workstations, matrix):
        self.jobs = jobs
        self.workstations = workstations
        self.matrix = matrix
        return

    def display(self):
        print("Jobs Number= ", self.jobs)
        print("Workstaion Number= ", self.workstations)
        for i in range(self.jobs):
            print(self.matrix[i])

    def build_workstation(self, index):
        jobs = self.build_jobs()
        return Workstation(index, jobs)

    def build_jobs(self):
        jobs= []
        for i in range(len(self.matrix)):
            jobs.append(Job(i, self.matrix[i][0], self.matrix[i]))
        return jobs


class Job:
    def __init__(self, index, arrival_time, length):
        self.finished = False
        self.index = index
        self.arrival = arrival_time
        self.lengths = length
        self.time_done = -1
        return

    def display(self):
        print("############################")
        print("finished = ", self.finished)
        print("index = ", self.index)
        print("arrival = ", self.arrival)
        print("time done = ")
        for i in range(len(self.lengths)):
            print(self.lengths[i])


class Workstation:
    def __init__(self, index, jobs):
        self.index = index
        self.jobs = jobs
        self.time = 0
        self.left_jobs = len(jobs)
        return

    def display(self):
        print("###########################")
        print("Workstation #", self.index)
        print("Time = ", self.time)
        print("Left Jobs = ", self.left_jobs)
        print("Jobs = ")
        for i in range(len(self.jobs)):
            self.jobs[i].display()

    def get_ready_jobs(self, time):
        ready_jobs = []
        for job in self.jobs:
            if job.arrival <= time and not job.finished:
                ready_jobs.append(job.index)
        return ready_jobs

    def shortest_job(self, job_ids):
        min2 = 1998
        min_id = -1
        for i in range (len(job_ids)):
            if self.jobs[job_ids[i]].lengths[self.index + 1] < min2:
                min_id = i
                min2 = self.jobs[job_ids[i]].lengths[self.index + 1]
        return min_id

    def do_job(self, job_id):
        self.left_jobs -= 1
        self.jobs[job_id].finished = True
        self.jobs[job_id].time_done = self.time
        self.time += self.jobs[job_id].lengths[self.index + 1]

    def workload(self):
        for i in range(self.left_jobs):
            ready = self.get_ready_jobs(self.time)
            if len(ready) is not 0:
                self.do_job(ready[self.shortest_job(ready)])
            else:
                self.time += 1
            ready.clear()
        return
