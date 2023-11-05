class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        def flip(k):
            L, R = 0, k - 1
	
            while L < R:
                arr[L], arr[R] = arr[R], arr[L]
                L += 1
                R -= 1
                
            return arr

        def find_max_elem_idx(L, R):
            idx, max_elem = None, -inf
            for i in range(L, R+1):
                if arr[i] > max_elem:
                    idx = i
                    max_elem = arr[i]

            return idx
        
        n = len(arr)
        res = []
        while n > 0:
            max_elem_idx = find_max_elem_idx(0, n-1)
            flip(max_elem_idx + 1)
            flip(n)
            res.append(max_elem_idx + 1)
            res.append(n)
            n -= 1

        return res
