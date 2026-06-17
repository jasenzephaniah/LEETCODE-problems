class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums[:] = nums[-k:] + nums[:-k]
