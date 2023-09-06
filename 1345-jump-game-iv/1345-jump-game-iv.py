class Solution:
    def minJumps(self, arr: List[int]) -> int:
        def check_and_jump(curr_idx, queue, visited):
            if curr_idx not in visited:
                queue.append(curr_idx)
                visited.add(curr_idx)
                
        n = len(arr)
        value_map = defaultdict(list)
        
        for i, val in enumerate(arr):
            value_map[val].append(i)

        queue, visited = deque([0]), set([0])
        visited.add(0)
        jumps = 0

        while queue:
            for _ in range(len(queue)):
                curr_idx = queue.popleft()
                prev, next = curr_idx - 1, curr_idx + 1

                if curr_idx == n - 1:
                    return jumps
                
                if prev >= 0:
                    check_and_jump(prev, queue, visited)
                if next < n:
                    check_and_jump(next, queue, visited)
                

                for nbr_idx in value_map[arr[curr_idx]]:
                    if nbr_idx not in visited:
                        queue.append(nbr_idx)
                        visited.add(nbr_idx)
                        
                value_map[arr[curr_idx]].clear()
            jumps += 1

                