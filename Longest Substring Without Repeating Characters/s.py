def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        end = 0
        start = 0
        c_max = 0
        cur = 0
        dic = {}
        while end <= len(s)-1: # Move window end forward
            if s[end] not in dic:
                dic[s[end]] = end # save index of this characters occurrence
                cur = end - start + 1
                if cur > c_max: # update the maximum if greater
                    c_max = cur
                
            else:
                while s[start] != s[end]: # Move window start forward until occurrence of s[end]
                    dic.pop(s[start])
                    start += 1
                dic[s[end]]=end
                start += 1

            end +=1 # move end of window forward

        return c_max
