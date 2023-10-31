class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        num1_count = Counter(arr1)
        res = []
        
        for num2 in arr2:
            res.extend([num2]*num1_count[num2])
            num1_count.pop(num2)
            
            
        for num in sorted(num1_count):
            res.extend([num]*num1_count[num])
            
        return res