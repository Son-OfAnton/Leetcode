class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        left = 0
        right = 0
        res = []
        
        while right < n:
            if chars[left] == chars[right]:
                right += 1
            else:
                res.append(chars[left])
                if right - left > 1:
                    for c in str(right - left):
                        res.append(c)
                left = right
                
        res.append(chars[left])
        if right - left > 1:
            for c in str(right - left):
                res.append(c)
        chars.clear()
        for c in res:
            chars.append(c)
        
        
        return len(res)
                
        