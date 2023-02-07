class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int, version1.split('.')))
        version2 = list(map(int, version2.split('.')))
        len_v1 = len(version1)
        len_v2 = len(version2)
        
        for i in range(max(len_v1, len_v2)):
            if i >= len_v1:
                digit_1 = 0
            else:
                digit_1 = version1[i]
            
            if i >= len_v2:
                digit_2 = 0
            else:
                digit_2 = version2[i]
                
            if digit_1 > digit_2:
                return 1
            elif digit_1 < digit_2:
                return -1
            
        return 0
        
       
