# Two-pointer solution. O(NM) run-time, where N is average word length and M is number of words in the list.
class Solution:
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        res = 0
        for word in words:
            if len(word) > len(S): continue
            s_l, s_r = 0, 0
            w_l, w_r = 0, 0
            flag = False
            while w_r < len(word) and s_r < len(S):
                if word[w_l] != S[s_l]:
                    break
                while s_r < len(S) and S[s_r] == S[s_l]:
                    s_r += 1
                while w_r < len(word) and word[w_r] == word[w_l]:
                    w_r += 1
                if s_r - s_l < 3 and w_r - w_l != s_r - s_l:
                    flag = True
                    break
                w_l = w_r
                s_l = s_r
            if flag: continue
            if w_r == len(word) and s_r == len(S): res += 1
        return res
           
