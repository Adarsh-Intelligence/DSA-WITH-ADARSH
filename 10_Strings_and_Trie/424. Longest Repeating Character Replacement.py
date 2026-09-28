class Solution(object):
    def characterReplacement(self, s, k):
        i = 0
        max_legth = 0
        max_frequecy = 0
        count =  {}

        for j in range(len(s)):
            count[s[j]] = count.get(s[j],0) + 1

            max_frequecy = max(max_frequecy , count[s[j]])

            if (j-i+1) - max_frequecy > k:
                count[s[i]] -=1
                i +=1
            max_legth = max(max_legth , j-i+1)
        return max_legth  