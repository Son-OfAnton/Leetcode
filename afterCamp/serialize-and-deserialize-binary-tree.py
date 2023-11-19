# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serialized = []

        def preorder(node):
            if not node:
                serialized.append('#')
                return
            
            serialized.append(str(node.val))
            serialized.append(',')
            preorder(node.left)
            preorder(node.right)
            
        preorder(root)
            
        return "".join(serialized)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.index = 0
        
        def decoder(start):
            if data[self.index] == '#':
                self.index += 1
                return None
            
            while data[self.index] != ',':
                self.index += 1
                
            node = TreeNode(int(data[start:self.index]))
            self.index += 1
            
            node.left = decoder(self.index)
            node.right = decoder(self.index)
            
            return node
            
        return decoder(0)
                

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))