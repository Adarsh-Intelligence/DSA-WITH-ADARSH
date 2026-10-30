class Solution(object):
    def isIsomorphic(self, s, t):

        group_st = {}
        group_ts = {}

        for i in range(len(s)):

            if s[i] in group_st and group_st[s[i]] != t[i]:
                return False

            if t[i] in group_ts and group_ts[t[i]] != s[i]:
                return False

            group_st[s[i]] = t[i]
            group_ts[t[i]] = s[i]

        return True


        