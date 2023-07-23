class Solution:
    def intToRoman(self, num: int) -> str:
        _map = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M',
               4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM'}
        
        roman = []
        
        exp = 0
        while num:
            x = num % 10
            x *= 10**exp
            exp += 1
            num //= 10
            
            if x == 0:
                continue
            if x in _map:
                roman.append(_map[x])
            elif x < 5:
                roman.extend(['I'] * x)
            elif x < 10:
                roman.extend(['I'] * (x - 5))
                roman.append('V')
            elif x < 50:
                roman.extend(['X'] * (x // 10))
            elif x < 100:
                roman.extend(['X'] * ((x - 50) // 10))
                roman.append('L')
            elif x < 500:
                roman.extend(['C'] * (x // 100))
            elif x < 1000:
                roman.extend(['C'] * ((x - 500) // 100))
                roman.append('D')
            else:
                roman.extend(['M'] * (x // 1000))
                
        return "".join(reversed(roman))