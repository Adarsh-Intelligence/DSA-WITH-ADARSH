class Solution(object):
    def findAnagrams(self, s, p):
        i = 0
        ans = []
        
        if len(p) > len(s):
            return ans

        count_p = {}
        count_window = {}

        for ch in p:
            count_p[ch] = count_p.get(ch, 0) + 1

        for j in range(len(s)):

            count_window[s[j]] = count_window.get(s[j], 0) + 1

            if j - i + 1 == len(p):

                if count_window == count_p:
                    ans.append(i)

                count_window[s[i]] -= 1

                if count_window[s[i]] == 0:
                    del count_window[s[i]]

                
                i += 1

        return ans