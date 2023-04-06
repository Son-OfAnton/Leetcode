class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj_set = defaultdict(set)
        
        for v_1, v_2 in roads:
            adj_set[v_1].add(v_2)
            adj_set[v_2].add(v_1)
                        
        max_net_rank = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                curr_rank = len(adj_set[i]) + len(adj_set[j])
                
                if i in adj_set[j]:
                    curr_rank -= 1
                    
                max_net_rank = max(max_net_rank, curr_rank)
                
        return max_net_rank
                
        