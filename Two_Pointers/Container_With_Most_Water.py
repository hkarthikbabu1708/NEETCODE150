# You are given an integer array heights where heights[i] represents the height of the ith bar
# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

def maxArea(height):
    max_area = float("-inf")
    l = 0
    r = len(height) - 1

    while l < r:
        curr_area = (r-l) * min(height[l], height[r])
        max_area = max(curr_area, max_area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area



height = [1,7,2,5,4,7,3,6]
print(maxArea(height))