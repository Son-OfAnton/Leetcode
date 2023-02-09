class Solution:
    def compress(self, chars: List[str]) -> int:
        right, left = 0, 0
        size = len(chars)
        
        while right < size:
            digit_spot = right
            
            while right < size and chars[right] == chars[digit_spot]:
                right += 1
                
            chars[left] = chars[digit_spot]
            left += 1
            
            if right - digit_spot != 1:
                for s in str(right - digit_spot):
                    chars[left] = s
                    left += 1
        return left     