from collections import deque  
        
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def DFS_preorder_rec(root) : 
    if not root : return 
    # process node 
    print(root.val,end='->')
    DFS_preorder_rec(root.left)
    DFS_preorder_rec(root.right)
    
def DFS_inorder_rec(root) : 
    if not root : return 
    # process node 
    DFS_inorder_rec(root.left)
    print(root.val,end='->')
    DFS_inorder_rec(root.right)
    
def DFS_postorder_rec(root) : 
    if not root : return 
    # process node 
    DFS_postorder_rec(root.left)
    DFS_postorder_rec(root.right)
    print(root.val,end='->')
    
def DFS_preorder_iter(root) : 
    if not root : return root 
    stack = [root]
    while stack : 
        current = stack.pop()
        print(current.val,end='->')
        if current.right : stack.append(current.right)
        if current.left : stack.append(current.left)
    print("")
    
def DFS_inorder_iter(root) : # left -> root -> right 
    if not root : return root 
    stack = []
    current = root
    while stack or current : 
        while current : 
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.val,end='->')
        current = current.right 
    print("")
    
def DFS_postorder_iter(root) : # left -> right -> root 
    if not root : return root 
    stack = [(root,False)]
    while stack : 
        current, visited = stack.pop()
        if visited : 
            print(current.val,end='->')
        else : 
            stack.append((current,True)) # save for later
            if current.right : stack.append((current.right,False))
            if current.left :stack.append((current.left,False))
    print("")
    
def BFS(root) : # Level Order traversal 
    if not root : return root 
    q = deque([root])
    while q : 
        current = q.popleft()
        print(current.val,end= "->")
        if current.left : q.append(current.left)
        if current.right : q.append(current.right)
# Max Height 
def max_height(root) : 
    if not root : return 0
    left = max_height(root.left)
    right = max_height(root.right)
    return 1 + max(left,right)
def max_height(root) : 
    q = deque([root])
    max_height = 0 
    while q : 
        level_width= len(q)
        for _ in range (level_width) : 
            curr = q.popleft()
            if curr.left : q.append(curr.left)
            if curr.right : q.append(curr.right)
        max_height +=1
    return max_height

# isSameTree
def isSameTree(p: Node, q: Node) -> bool :# O(n) O(h)
    if not p and not q : return True 
    if not p or not q : return False 
    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right) 
def isSameTree(p: Node, q: Node) -> bool : 
    if not p and not q : return True 
    if not p or not q : return False 
    q1 = deque([p])
    q2 = deque([q])
    while q1 and q2 : 
        curr1 = q1.popleft()
        curr2 = q2.popleft()
        if curr1.val != curr2.val : return False
        if curr1.left and curr2.left : 
            q1.append(curr1.left)
            q2.append(curr2.left)
        elif curr1.left or curr2.left :
            return False 
        if curr1.right and curr2.right : 
            q1.append(curr1.right)
            q2.append(curr2.right)
        elif curr1.right or not curr1.right :
            return False 
    return not q1 and not q2 
def isSameTree(p: Node, q: Node) -> bool :
    if not p and not q : return True 
    if not p or not q : return False 
    q1 = deque([p])
    q2 = deque([q])
    while q1 and q2 : 
        curr1 = q1.popleft()
        curr2 = q2.popleft()
        if not curr1 and not curr2 : continue 
        elif not curr1 or not curr2 : return False    
        if curr1.val != curr2.val : return False
        q1.append(curr1.left)
        q2.append(curr2.left)
        q1.append(curr1.right)
        q2.append(curr2.right)
    return not q1 and not q2 
# Inverse a binary tree 
def inversTree(root) : 
    if not root : return 
    inversTree(root.left)
    inversTree(root.right)
    # process root
    root.left , root.right = root.right , root.left 
    
def inversTree(root) : 
    if not root : return root 
    q = deque([root])
    while q : 
        curr = q.popleft()
        curr.left, curr.right = curr.right,curr.left
        if curr.left : 
            q.append(curr.left)
        if curr.right :
            q.append(curr.right)
            
def LCA(root,p,q) : 
    if not root or root is q or root is p : 
        return root 
    left =  LCA(root.left,p,q)
    right = LCA(root.right,p,q)
    if left and right : 
        return root 
    return left if left else right  

def LCA(root,p,q) : 
    if not root : return root 
    q = deque([root])
    parent = {root:None}
    while p not in parent or q not in parent : 
        curr = q.popleft()
        if curr.left : 
            parent[curr.left] = curr
            q.append(curr.left)
        if curr.right : 
            parent[curr.right] = curr
            q.append(curr.right)
    curr = p 
    ancesstors = set()
    while curr : 
        ancesstors.add(curr)
        curr = parent[p]
    curr = q 
    while curr not in ancesstors : 
        curr = parent[curr]
    return curr
def LCA(root,p,q) : 
    if not root : return root 
    stack =  [root]
    parent = {root:None}
    while p not in parent or q not in parent : 
        curr = stack.pop()
        if curr.right : 
            parent[curr.right] = curr
            q.append(curr.right)
        if curr.left : 
            parent[curr.left] = curr
            q.append(curr.left)
    curr = p 
    ancesstors = set()
    while curr : 
        ancesstors.add(curr)
        curr = parent[curr]
    curr = q 
    while curr not in ancesstors : 
        curr = parent[curr]
    return curr 

def path_to_node(root,node) :
    result = [root]
    stack = [(root,[])]
    while stack : 
        curr , path_to_curr = stack.pop()
        if curr is node : return path_to_curr + [curr]
        if curr.right : 
            stack.append((curr.right,path_to_curr + [curr]))
        if curr.left : 
            stack.append((curr.left,path_to_curr + [curr]))

    
def LCA(root,p,q) : 
    path_p = path_to_node(root,p)
    path_q = path_to_node(root,q)
    i = 0 
    while i<len(path_p) and i< len(path_q) and path_p[i] == path_q[i] : 
        i+=1 
    return path_q[i-1]

# when BST
def LCA_BST(root,p,q) : 
    if not root or not p or not q  : return root 
    current = root 
    while current : 
        if p.val<root.val and q.val<root.val : 
            current = current.left   
        if p.val>root.val and q.val>root.val : 
            current = current.right
        else : 
            return current 

# Tree Diameter
def tree_diameter(root) : # O(n)
    global diameter 
    diameter = 0 
    def dfs(root) : 
        if not root : return 0 
        left = dfs(root.left)
        right = dfs(root.right)
        diameter = max(diameter,left+right)
        return 1 + max(left,right)
def tree_diameter(root) : # O(n^2)
    if not root : return 0 
    left = max_height(root.left)
    right = max_height(root.right)
    return max(left+right,tree_diameter(root.left), tree_diameter(root.right))

def is_balanced(root) :  # Balanced Tree : naive solution O(n^2) O(h)
    if not root : return True 
    left = max_height(root.left)
    right = max_height(root.right)
    if abs(left - right > 1) : return False 
    return  is_balanced(root.left) and is_balanced(root.right) 
def is_balanced(root) : # Balanced Tree : single traversal O(n) O(h)
    def dfs(root) :
        if not root : return 0 
        left = dfs(root.left)
        right = dfs(root.right)
        if left - right > 1 or left == -1 or right == -1 :
            return -1 
        return 1 + max(left,right) 
    return dfs(root) != -1 
# path_sum : recursive O(n) O(h)
def path_sum(root,target) : 
    if not root : return False 
    if not root.left and not root.right : 
        if root.val == target.val : return True
    return path_sum(root.left,target-root.val) or path_sum(root.right,target-root.val)
# path_sum : iterative stack O(n) O(h)
def path_sum(root,target) : 
    stack = [(root,root.val)]
    while stack : 
        curr, curr_sum = stack.pop()
        if not curr.right and not curr.left : 
            if curr_sum == target : return True   
        if curr.right : 
            stack.append((curr.right,curr_sum+curr.right.val))
        if curr.left : 
            stack.append((curr.right,curr_sum+curr.right.val))
    return False 
def max_path_sum(root) :
    global max_sum 
    max_sum = float("-inf")
    def dfs(root) : 
        if not root : return 0
        left = max(0,dfs(root.left)) 
        right = max(0,dfs(root.right)) 
        max_sum = max(max_sum,root.val+left+right)
        return root.val +  max(left,right)
    dfs(root)
    return max_sum
