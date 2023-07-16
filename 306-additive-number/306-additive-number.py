class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(a, b, c):
            if(len(a) > 1 and a[0] == '0') \
                or (len(b) > 1 and b[0] == '0') \
                or (len(c) > 1 and c[0] == '0'):
                return False

            target_sum = str_sum(a, b)
            if target_sum == c:
                return True
            
            n = len(target_sum)
            if len(c) <= n:
                return False
            
            if target_sum == c[:n]:
                return dfs(b, target_sum, c[n:])
            else:
                return False

        def str_sum(a, b):
            sum_digits = []
            i, j = len(a) - 1, len(b) - 1
            carry_one = 0

            while i >= 0 and j >= 0:
                carry_one, place_val = divmod(int(a[i]) + int(b[j]) + carry_one, 10)
                sum_digits.append(str(place_val))
                i -= 1
                j -= 1
            
            while i >= 0:
                carry_one, place_val = divmod(int(a[i]) + carry_one, 10)
                sum_digits.append(str(place_val))
                i -= 1

            while j >= 0:
                carry_one, place_val = divmod(int(b[j]) + carry_one, 10)
                sum_digits.append(str(place_val))
                j -= 1

            if carry_one:
                sum_digits.append('1')
            
            return ''.join(sum_digits[::-1])
        
        if num == '0000':
            return True

        for i in range(len(num)):
            for j in range(i):
                a = num[:j+1]
                b = num[j+1:i+1]
                c = num[i+1:]

                if dfs(a, b, c):
                    return True

        return False

