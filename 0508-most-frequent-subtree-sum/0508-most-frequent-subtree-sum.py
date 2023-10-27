# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sum_freq = defaultdict(int)
        
        def dfs(node):
            if not node:
                return 0
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            curr_node_sum = left_sum + right_sum + node.val
            
            sum_freq[curr_node_sum] += 1
            return curr_node_sum
            
        
        dfs(root)
        res = []
        max_freq_sum = max(sum_freq.values())
        
        for summ, freq in sum_freq.items():
            if freq == max_freq_sum:
                res.append(summ)
                
        return res
            