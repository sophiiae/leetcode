class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ''
        tmp = ''
        for i, ch in enumerate(s):
            if (ch in tmp):
                tmp = tmp[tmp.find(ch) + 1:] + ch
            else:
                tmp = tmp + ch
            longest = tmp if len(tmp) > len(longest) else longest
        return len(longest)
