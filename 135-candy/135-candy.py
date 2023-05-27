class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy_num = [1 for _ in range(n)]

        for i in range(1, n):
            if ratings[i]  > ratings[i - 1]:
                candy_num[i] = max(candy_num[i], candy_num[i - 1] + 1)
        
        for i in range(n - 2, -1, -1):
            if ratings[i]  > ratings[i + 1]:
                candy_num[i] = max(candy_num[i], candy_num[i + 1] + 1)

        return sum(candy_num)