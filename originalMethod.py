import itertools
import time

class num:
    def __init__(self, x, route=None):
        self.x = x
        if route is None:
            self.route = x
        else:
            self.route = route
    
    def __add__(self, b):
        return num(self.x + b.x, (self.route, '+', b.route))
    
    def __sub__(self, b):
        return num(self.x - b.x, (self.route, '-', b.route))
    
    def __mul__(self, b):
        return num(self.x * b.x, (self.route, '*', b.route))
    
    def __truediv__(self, b):
        if b.x == 0:
            return num(0)
        return num(self.x / b.x, (self.route, '/', b.route))
    
    def __eq__(self, b):
        return self.x == b.x
    
    def __repr__(self):
        return f'NUM: {self.x} = {self.route}'

cache = {}
def E(S):
    key = tuple(sorted(s.x for s in S))  # subsets with same numbers
    if key in cache:
        return cache[key]
    
    l = len(S)
    if l == 1:
        return S
    elif l == 2:
        a, b = S
        solutions = [a + b, a - b, b - a, a * b, a / b, b / a]
        cache[key] = solutions
        return solutions
    else:
        solutions = []
        for A in itertools.chain.from_iterable(itertools.combinations(S, a_r) for a_r in range(l//2, l)):
            Q = [s for s in S if s not in A]
            for B in itertools.chain.from_iterable(itertools.combinations(Q, r_b) for r_b in range(1, l//2 + 1)):
                eA = E(A)
                eB = E(B)
                for a,b in itertools.product(eA, eB):
                    solutions.extend([a*b, a/b, b/a, a+b, a-b, b-a])

        cache[key] = solutions
        return solutions
    
def solve(initial_numbers, goal):
    anwsers = E(list(map(num, initial_numbers)))
    solutions = [ans.route for ans in anwsers if ans.x == goal]
    return solutions


start = time.time()
sols = solve([2, 4, 5, 6, 10, 50], 941)
end = time.time()
print(f'found {len(sols)} solutions in {(end - start):.2f}s:')
print(*sols, sep='\n')
