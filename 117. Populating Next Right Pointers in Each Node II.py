class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self.dfs(root)
        return root    
    
    
    def dfs(self, root: 'Node'):
        if root:
            if root.left:
                root.left.next = root.right if root.right else self.helper(root.next)
            if root.right:
                root.right.next = self.helper(root.next)

            self.dfs(root.right)
            self.dfs(root.left)
            
            
    def helper(self, root: 'Node') -> 'Node':
        if not root:
            return None
        else:
            return root.left if root.left else root.right if root.right else self.helper(root.next)
