class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n <= 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                l = flowerbed[i - 1] if i != 0 else 0
                r = flowerbed[i + 1] if i != len(flowerbed) - 1 else 0
                if l == 0 and r == 0:
                    flowerbed[i] = 1
                    n -= 1
                if n == 0:
                    return True
        return False
