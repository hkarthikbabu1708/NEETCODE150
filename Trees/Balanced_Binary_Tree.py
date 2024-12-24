# Given a binary tree, return true if it is height-balanced and false otherwise.
#
# A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in
# height by no more than 1.

def isBalanced(root):
    if not root:
        return True

    stack = [(root, False)]
    heights = {}

    while stack:
        node, visited = stack.pop()

        if node is None:
            continue

        if visited:
            left_height = heights.get(node.left, 0)
            right_height = heights.get(node.right, 0)

            if abs(left_height - right_height) > 1:
                return False
            heights[node] - max(left_height, right_height) + 1

        else:
            stack.append(node, True)
            stack.append(node.left, False)
            stack.append(node.right, False)

    return True