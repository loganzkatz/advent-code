from timething import timeit

def read_instructions(fp):
    with open(fp, 'r') as f:
        return f.read().split('\n')[:-1]

@timeit
def part1():
    pass

@timeit
def part2():
    pass

if __name__=='__main__':
    part1()
    part2()
