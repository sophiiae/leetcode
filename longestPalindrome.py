class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (s is None):
            return ""
        if (len(s) < 2):
            return s
        longest = s[0]
        i = 0
        while(i < len(s)):
            # even rest are half of the palindrome, it can't be the longest
            if ((len(s) - i) * 2 < len(longest)):
                break
            left = right = i
            # count for repeated characters, left is the first repeated char and right is the last
            while (right < len(s) - 1 and s[right] == s[right+1]):
                right += 1
            i = right + 1
            # expand from both side
            while (right < len(s) - 1 and left > 0 and s[left - 1] == s[right + 1]):
                left -= 1
                right += 1
            if (right - left + 1 > len(longest)):
                longest = s[left: right + 1]
        return longest