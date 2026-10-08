class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        if goal == 0:
            count = 0
            zeros = 0

            for num in nums:
                if num == 0:
                    zeros += 1
                    count += zeros
                else:
                    zeros = 0

            return count

        i = 0
        currant_sum = 0
        count = 0
        zero_count = 0

        for j in range(len(nums)):
            currant_sum += nums[j]

            while currant_sum > goal:
                currant_sum -= nums[i]
                i += 1
                zero_count = 0

            while i <= j and nums[i] == 0:
                zero_count += 1
                i += 1

            if currant_sum == goal:
                count += zero_count + 1

        return count
        
        

            
        
        