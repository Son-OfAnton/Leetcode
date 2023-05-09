from heapq import heappush, heappop, heapify

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        nums1_bound, nums2_bound = min(k, len(nums1)),  min(k, len(nums2))

        for i in range(nums1_bound):
            for j in range(nums2_bound):
                curr_sum = nums1[i] + nums2[j]
                if len(heap) < k:
                    heappush(heap, (-curr_sum, [nums1[i], nums2[j]]))
                elif curr_sum < -heap[0][0]:
                    heappop(heap)
                    heappush(heap, (-curr_sum, [nums1[i], nums2[j]]))
                # there is no point finding other pairs since the possible
                # pairs after this point has a sum greater than the max sum
                # we currently have
                else:
                    break

        return [pair[1] for pair in heap]