import fileinput
from data import Data


def get_data(file_name):
    # READ INPUT FROM FILE
    input = fileinput.input(file_name)
    # READ FIRST LINE AN ASSIGN IT
    text = input[0].replace('\n', '').split(' ')
    jobs = int(text[0])
    workstations = int(text[1])
    # READ OTHER LINES
    t = []
    for line in input:
        line_numbers = [int(jobs) for jobs in line.split()]
        t.append(line_numbers)
    return Data(jobs, workstations, t)
