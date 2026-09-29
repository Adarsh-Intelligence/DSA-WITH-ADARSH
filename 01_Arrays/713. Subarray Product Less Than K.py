class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
    
        if k <= 1:
            return 0

        i = 0
        product = 1
        count = 0
        for j in range(len(nums)):
            product *= nums[j]

            while product >=k:
                product //= nums[i]
                i+=1

            count += j - i + 1
        return count
        