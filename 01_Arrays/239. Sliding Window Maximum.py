from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        result = []
        i = 0

        for j in range(len(nums)):
            while dq and nums[dq[-1]] <= nums[j]:
                dq.pop()

            dq.append(j)

            if dq[0] < i:
                dq.popleft()

            if j - i + 1 == k:
                result.append(nums[dq[0]])
                i += 1

        return result