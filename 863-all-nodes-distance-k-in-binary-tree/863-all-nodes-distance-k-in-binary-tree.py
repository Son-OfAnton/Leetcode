# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def preorder(node, parent=None):
            if not node:
                return

            if parent:
                graph[node.val].append(parent.val)
            if node.left:
                graph[node.val].append(node.left.val)
            if node.right:
                graph[node.val].append(node.right.val)
                
            preorder(node.left, node)
            preorder(node.right, node)

        preorder(root)
        nodes_at_k_dist = []
        queue, visited = deque([(target.val, 0)]), set([target.val])

        while queue:
            node, dist = queue.popleft()
            
            if dist == k:
                nodes_at_k_dist.append(node)
            if dist > k:
                break

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append((neighbour, dist + 1))
                    visited.add(neighbour)
                    
        return nodes_at_k_dist