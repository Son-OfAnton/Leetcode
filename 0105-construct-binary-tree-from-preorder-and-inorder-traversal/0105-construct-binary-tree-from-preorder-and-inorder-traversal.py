class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def build_tree(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            root_idx = inorder_idx_map[root_val]
            left_size = root_idx - in_start
            
            root.left = build_tree(pre_start+1, pre_start+left_size, in_start, root_idx-1)
            root.right = build_tree(pre_start+left_size+1, pre_end, root_idx+1, in_end)
            
            return root

        n = len(preorder)
        inorder_idx_map = {val:i for i, val in enumerate(inorder)}
        return build_tree(0, n - 1, 0, n - 1)