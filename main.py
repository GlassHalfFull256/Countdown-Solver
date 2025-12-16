import itertools
import operator

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
        return num(self.x / b.x, (self.route, '/', b.route))
    
    def __float__(self):
        return float(self.x)
    
    def __eq__(self, b):
        if type(b) == int:
            return self.x == b
        else:
            return self.x == b.x
        
    def R(self, expr):
        if type(expr) == tuple:
            return f'({self.R(expr[0])} {expr[1]} {self.R(expr[2])})'
        else:
            return expr
    
    def __repr__(self):
        return self.R(self.route)
    
def solve(start_numbers, goal, operators):
    cache = set()
    stack = [tuple(map(num, start_numbers))]
    while stack:
        S = stack.pop()
        if len(S) == 1:
            if abs(S[0].x - goal) < 1e-6:
                print(S[0])
            continue
        if goal in S:
            print([s for s in S if s == goal][0])
        for a, b in itertools.combinations(S, 2):
            R = tuple(x for x in S if x not in (a, b))
            for op in operators:
                try:
                    result = op(a, b)
                except ZeroDivisionError:
                    continue
                Q = R + (result,)
                Qs = tuple(sorted(map(float, Q)))
                if Qs not in cache:
                    cache.add(Qs)
                    stack.append(Q)

if __name__ == '__main__':
    operators = (operator.add, operator.sub, operator.mul, operator.truediv, lambda a, b: b - a, lambda a, b: b/a)
    start_numbers = tuple(map(int, input('Starting numbers (Use \' \' as a delimiter): ').split()))
    goal = int(input('Goal: '))
    solve(start_numbers, goal, operators)