from collections import deque
# If the tree is empty:
#     return an empty list

# Create an empty queue
# Create an empty list to store visited nodes

# Add the root into the queue

# While the queue is not empty:
#     Pop the next node off the queue 
#     Add the popped node to the list of visited nodes

#     Add the popped node's left child to the queue
#     Add the popped node's right child to the queue

def bfs(root):
    if not root:
        return []
    
    visited = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        visited.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return visited


def dfs_preorder(root):
    if not root:
        return []

    visited = []
    stack = [root]

    while stack:
        node = stack.pop()
        visited.append(node.val)

        # Push right first so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return visited

def dfs_preorder(root):
    if not root:
        return []
    return [root.val] + dfs_preorder(root.left) + dfs_preorder(root.right)


def dfs_inorder(root):
    if not root:
        return []
    return dfs_inorder(root.left) + [root.val] + dfs_inorder(root.right)


def dfs_postorder(root):
    if not root:
        return []
    return dfs_postorder(root.left) + dfs_postorder(root.right) + [root.val]

