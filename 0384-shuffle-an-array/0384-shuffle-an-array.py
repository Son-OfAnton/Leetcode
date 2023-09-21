class Solution:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.original = nums
        self.nums = nums[:]        

    def reset(self) -> List[int]:
        return self.original
        

    def shuffle(self) -> List[int]:
        for i in range(self.n):
            rand_idx = random.randrange(i, self.n)
            self.nums[i], self.nums[rand_idx] = self.nums[rand_idx], self.nums[i]
            return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()