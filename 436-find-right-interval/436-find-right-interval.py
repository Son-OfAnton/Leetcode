class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        start_idx = []
        
        for idx, interval in enumerate(intervals):
            start_idx.append((interval[0], idx))
        
        start_idx.sort()
        right_intervals = []
        
        for start, end in intervals:
            left = 0
            right = n - 1

            while left <= right:
                mid = left + (right - left) // 2
                
                if start_idx[mid][0] < end:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            if left == n:
                right_intervals.append(-1)
            else:
                right_intervals.append(start_idx[left][1])
                
        return right_intervals
                    
                


        
        
        
        
        
        
        
        
        
        
        
        