class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    #recursive approach
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + (max(self.maxDepth(root.left, ), self.maxDepth(root.right)))

    def maxepth(self, root):
        # iterative approach
        if not root:  # Handle empty tree
            return 0

        stack = [(root, 1)]  # Stack holds (node, current_depth)
        max_depth = 0

        while stack:
            curr, depth = stack.pop()  # Unpack the tuple
            if curr:
                max_depth = max(max_depth, depth)
                # Push children onto the stack with incremented depth
                stack.append((curr.left, depth + 1))
                stack.append((curr.right, depth + 1))

        return max_depth


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)

solution = Solution()
depth = solution.maxDepth(root)
print(f"The maximum depth of the binary tree is: {depth}")

solution = Solution()
depth = solution.maxepth(root)
print(f"The maximum iterative depth of the binary tree is: {depth}")

