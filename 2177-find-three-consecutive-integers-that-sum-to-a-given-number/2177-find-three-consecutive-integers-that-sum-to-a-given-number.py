class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        res = []
        first_num = (num - 3) / 3
        ceil = math.ceil(first_num)
        
        if ceil - first_num != 0:
            return res
        else:
            for i in range(3):
                res.append(int(first_num + i))
                
            return res
        