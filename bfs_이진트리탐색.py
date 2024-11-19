from collections import deque



def bfs_binary_tree(root):
    if not root:
        return []
    
    queue = deque([root])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(bfs_binary_tree(root))