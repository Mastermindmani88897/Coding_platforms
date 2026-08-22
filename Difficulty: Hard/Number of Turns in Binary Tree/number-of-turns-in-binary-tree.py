class Solution:
    def numberOfTurns(self, root, p, q):
        def find_path(node, target, path):
            if not node:
                return False
    
            if node.data == target:
                return True
    
            path.append('L')
            if find_path(node.left, target, path):
                return True
            path.pop()
    
            path.append('R')
            if find_path(node.right, target, path):
                return True
            path.pop()
    
            return False
    
        path_p = []
        path_q = []
    
        find_path(root, p, path_p)
        find_path(root, q, path_q)
    
        i = 0
        while i < len(path_p) and i < len(path_q) and path_p[i] == path_q[i]:
            i += 1
    
        turns = 0
    
        for j in range(i, len(path_p) - 1):
            if path_p[j] != path_p[j + 1]:
                turns += 1
    
        for j in range(i, len(path_q) - 1):
            if path_q[j] != path_q[j + 1]:
                turns += 1
    
        if i < len(path_p) and i < len(path_q):
            turns += 1
    
        return turns if turns > 0 else -1