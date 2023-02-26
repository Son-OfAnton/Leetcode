class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ptr_1 = ptr_2 = 0
        merged = []
        
        while ptr_1 < len(word1) and ptr_2 < len(word2):
            if word1[ptr_1] > word2[ptr_2]:
                merged.append(word1[ptr_1])
                ptr_1 += 1
            elif word1[ptr_1] < word2[ptr_2]:
                merged.append(word2[ptr_2])
                ptr_2 += 1
            else:
                if word1[ptr_1+1:] > word2[ptr_2+1:]:
                    merged.append(word1[ptr_1])
                    ptr_1 += 1
                else:
                    merged.append(word2[ptr_2])
                    ptr_2 += 1
                    
        while ptr_1 < len(word1):
            merged.append(word1[ptr_1])
            ptr_1 += 1
        while ptr_2 < len(word2):
            merged.append(word2[ptr_2])
            ptr_2 += 1
            
        return "".join(merged)