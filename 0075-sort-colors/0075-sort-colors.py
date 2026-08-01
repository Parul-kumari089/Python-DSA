class Solution:
    def sortColors(self, nums: List[int]) -> None:
        maximum = max(nums)
        count  = [0]*(maximum+1)
        for num in nums:
            count[num] += 1
        index = 0 
        for i in range(len(count)):
            while count[i] > 0 :
                nums[index] = i 
                index += 1
                count[i] -= 1
        return nums        