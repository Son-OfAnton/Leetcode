class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        queue, seen = deque([start]), set([start])
        
        while queue:
            curr = queue.popleft()
            
            if arr[curr] == 0:
                return True
            next, prev = curr + arr[curr], curr - arr[curr]
            if next < n and next not in seen:
                queue.append(next)
                seen.add(next)
            if prev >= 0 and prev not in seen:
                queue.append(prev)
                seen.add(prev)
                
        return False
                