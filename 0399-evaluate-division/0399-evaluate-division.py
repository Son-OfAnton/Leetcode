class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (numerator, denominator), val in zip(equations, values):
            graph[numerator].append((denominator, val))
            graph[denominator].append((numerator, 1/val))
                    
        res = []
        for numerator, denominator in queries:
            if numerator not in graph or denominator not in graph:
                res.append(-1.0)
                continue
            if numerator == denominator:
                res.append(1.0)
                continue
                
            queue = deque([(numerator, 1.0)])
            seen = set([numerator])
            operands_found = False
            
            while queue:
                curr, prod = queue.popleft()
                if curr == denominator:
                    operands_found = True
                    res.append(prod)
                    break
                
                for var, quotient in graph[curr]:
                    if var not in seen:
                        curr_prod = prod * quotient
                        queue.append((var, curr_prod))
                        seen.add(var)

            if not operands_found:
                res.append(-1.0)

                    
        return res
            

