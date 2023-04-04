class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
    
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        partition_size = 0
        
        for grouping in count.values():
            partition_size = self.gcd(grouping, partition_size)
            
        return partition_size > 1 
            