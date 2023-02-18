# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        middle = len(nums) // 2
        root = nums[middle]
        left_subtree = self.sortedArrayToBST(nums[:middle])
        right_subtree = self.sortedArrayToBST(nums[middle + 1:])
                                      
        return TreeNode(root, left_subtree, right_subtree)
    
# recursively partition nums and find the middle element of the partition. 
# Then assign the middle element as a root node to each subtree.