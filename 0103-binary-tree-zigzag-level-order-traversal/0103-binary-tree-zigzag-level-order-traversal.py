# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Queue:
    def __init__(self):
        self.q = []
        self.front = -1

    def push(self, x):
        if self.front == -1:
            self.front = 0
        self.q.append(x)

    def pop(self):
        if self.size() == 0:
            return -1

        x = self.q[self.front]
        self.front += 1

        if self.front == len(self.q):
            self.front = -1
            self.q = []

        return x

    def getFront(self):
        if self.size() == 0:
            return -1
        return self.q[self.front]

    def size(self):
        if self.front == -1:
            return 0
        return len(self.q) - self.front


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        queue = Queue()
        ans = []
        queue.push(root)
        left_to_right = True

        while queue.size() > 0:
            l = queue.size()
            level = []
            for i in range(l):
                node = queue.pop()
                level.append(node.val)
                if node.left is not None:
                    queue.push(node.left)
                if node.right is not None:
                    queue.push(node.right)
            if not left_to_right:
                level.reverse()
            ans.append(level)
            left_to_right = not left_to_right
        return ans