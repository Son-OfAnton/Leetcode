class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        no_of_trees = len(fruits)
        taken = defaultdict(int)
        left = 0
        
        for right in range(no_of_trees):
            taken[fruits[right]] += 1
            
            if len(taken) > 2:
                taken[fruits[left]] -= 1
                
                if taken[fruits[left]] == 0:
                    taken.pop(fruits[left])
                    
                left += 1
                
        return right - left + 1
