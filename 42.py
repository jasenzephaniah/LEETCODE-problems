class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        w = 0
        lmax = 0
        rmax = 0
        while left < right:
            if height[left] < height[right]:
                if lmax < height[left]:
                    lmax = height[left]
                else:
                    w += lmax - height[left]
                left += 1
            else:
                if rmax < height[right]:
                    rmax = height[right]
                else:
                    w += rmax - height[right]
                right -= 1
        return w
