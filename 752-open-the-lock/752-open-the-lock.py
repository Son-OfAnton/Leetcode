class Solution:
    def next_comb_generator(self, comb: str) -> List[str]:
        possible_comb = []

        for i in range(4):
            next_digit = str((int(comb[i]) + 1) % 10)
            next_num = comb[:i] + next_digit + comb[i+1:]
            prev_digit = str((int(comb[i]) - 1 + 10) % 10)
            prev_num = comb[:i] + prev_digit + comb[i+1:]
            possible_comb.append(next_num)
            possible_comb.append(prev_num)
            
        return possible_comb

    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        queue, visited = deque([("0000", 0)]), set(deadends)

        while queue:
            comb, turns = queue.popleft()
            if comb == target:
                return turns
        
            for next_comb in self.next_comb_generator(comb):
                if next_comb not in visited:
                    queue.append((next_comb, turns + 1))
                    visited.add(next_comb)

        return -1





            