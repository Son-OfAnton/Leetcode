class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        interim_res = self.countAndSay(n-1)
        i = 0
        res = []
        while i < len(interim_res):
            num = interim_res[i]
            freq = 0
            while i < len(interim_res) and interim_res[i] == num:
                freq += 1
                i += 1
            res.append(str(freq))
            res.append(num)

        return ''.join(res)
        
        
        