class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        for i in range(len(flowerbed)):

            if i == 0:
                left = True
            else:
                left = (flowerbed[i - 1] == 0)

            if i == len(flowerbed) - 1:
                right = True
            else:
                right = (flowerbed[i + 1] == 0)

            if flowerbed[i] == 0 and left and right:
                flowerbed[i] = 1
                count += 1

            if count >= n:
                return True

        return count >= n