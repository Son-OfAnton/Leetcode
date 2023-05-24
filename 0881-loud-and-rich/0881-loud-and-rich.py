# class Solution:
#     def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
#         MAX, n = float("inf"), len(quiet)
#         graph = defaultdict(list)
#         indegree = defaultdict(int)
#         for a, b in richer:
#             graph[b].append(a)
#             indegree[a] += 1

#         res = [None for _ in range(n)]
        
        
#         def top_sort(person):
#             if res[person] != None:
#                 return

#             for rich_conn in graph[person]:
#                 below_min, below_person = top_sort(rich_conn)
#                 print(f"node {person} bm {below_min} bp {below_person}")

#                 if below_min < quiet[person]:
#                     quiet[person] = below_min
#                     res[person] = below_person

#             return [quiet[person], res[person]]



#         for person in range(n):
#             if indegree[person] == 0:
#                 top_sort(person)

#         return res

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        richer_than_me, richer_quieter = [], []
        graph = defaultdict(list)
        
        for person in range(len(quiet)):
            richer_than_me.append(0)
            richer_quieter.append(person)
        
        for rich, poor in richer:
            graph[rich].append(poor)
            richer_than_me[poor] += 1
            
        queue = deque(person for person, count in enumerate(richer_than_me) if count == 0)

        while queue:
            person = queue.popleft()
            
            for poorer in graph[person]:
                richer_quieter[poorer] = min(richer_quieter[person], richer_quieter[poorer], key = lambda x : quiet[x])
                richer_than_me[poorer] -= 1

                if richer_than_me[poorer] == 0: # indegree == 0
                    queue.append(poorer)

        return richer_quieter