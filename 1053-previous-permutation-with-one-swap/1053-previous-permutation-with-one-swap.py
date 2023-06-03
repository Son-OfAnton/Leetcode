class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        
        # finding the first element from the right that breaks
        # a decreasing slope
        i = len(arr) - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1
        
        # if we pass 0, the arr was surely in non-increasing order
        if i < 0:
            return arr
        
        
        # now find the first number that right of i that is largest 
        # in arr[i+1:]
        j = len(arr) - 1
        while arr[j] >= arr[i]:
            j -= 1

        # there might multiple arr[j]s so take the left most of them 
        while arr[j] == arr[j - 1]:
            j -= 1

        arr[i], arr[j] = arr[j], arr[i]

        return arr
