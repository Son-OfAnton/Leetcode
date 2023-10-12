class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        count = 1
        
        for i in range(2, n+1):
            count = (count * ((2*i - 1) * i)) % MOD
            
        return count
    
# For a given n there are 2n positions to be filled by P1-Pn and D1-Dn.
# For those positions a pickup can have 2*i - 1 choices because it can't
# use the last place because it has to be delivered later. The deliveries
# has i potential spots to be placed. 