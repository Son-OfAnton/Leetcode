class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n, seen = len(graph), set()
        all_seen_mask = (1 << n) - 1
        queue = deque()

        for node in range(n):
            curr_node_mask = 1 << node
            seen.add((node, curr_node_mask))
            queue.append((node, curr_node_mask, 1))

        while queue:
            curr, curr_mask, path_len = queue.popleft()
            
            for nbr in graph[curr]:
                union_mask = curr_mask | 1 << nbr
                if union_mask == all_seen_mask:
                    return path_len
                if (nbr, union_mask) not in seen:
                    seen.add((nbr, union_mask))
                    queue.append((nbr, union_mask, path_len+1))

        return 0

# We can track the visited nodes by setting a bit of their place. 
# Then we will set the other nodes bit position and bit OR with 
# the previous one, this effectively joins the two visited node 
# information aka represents all nodes in that particular path. 
# If we arrive at a node with some mask which if formed before 
# that means we are about to repeat a path. So we can uniquely 
# track seen paths by a node and a mask at that node.