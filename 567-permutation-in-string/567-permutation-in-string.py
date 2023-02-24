class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size_1, size_2 = len(s1), len(s2)
        left = 0
        dic_1 = Counter(s1)
        dic_2 = defaultdict(int)
        
        for right in range(size_2):
            dic_2[s2[right]] += 1
            
            if right - left + 1 == size_1:
                if dic_1 == dic_2:
                    return True
                
                dic_2[s2[left]] -= 1
                
                if dic_2[s2[left]] == 0:
                    dic_2.pop(s2[left])
                
                left += 1
                    
        return False
    