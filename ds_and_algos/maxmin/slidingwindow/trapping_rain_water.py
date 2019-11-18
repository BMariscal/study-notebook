
# Find the maximum amount of rain water you can trap
def trap(height):
    if height == None:
        return 0

    # divide the water tower in half
    left = 0  # pointer to left-most index
    right = len(height) - 1  # pointer to right-most index
    left_max_height = 0  # keep track of the max-tower height on left-side
    right_max_height = 0  # keep track of the max-tower height on right-side
    water_trapped = 0

    # Left is initialized at left-most index
    # right is initialized at right-most index
    # continue while loop as long as left index is less than right index
    # The amount of water that's trapped is the difference between the tallest tower height on a given side and the current tower height on a given side
    # We advance the left window as long as height of the left tower(the tallest height we've encountered in the left window so far) is <= the height of the right tower (the tallest height encountered so far in the right window). The right window works the same way - we are always advancing the window that has the smaller maximum height
    while left < right:
        left_max_height = max(height[left], left_max_height)
        right_max_height = max(height[right], right_max_height)

        if left_max_height <= right_max_height:
            water_trapped += left_max_height - height[left]
            left += 1
        else:
            water_trapped += right_max_height - height[right]
            right -= 1
    return water_trapped