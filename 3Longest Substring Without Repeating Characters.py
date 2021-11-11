#problem description:
#Given a string s, find the length of the longest substring without repeating characters.

# use the concept of set, all the elements in a set should be unique.

class Solution:
    def lengthOfLongestSubstring(self,s):
        i=0
        j=0
        chars=set()
        maxstr=0
        for j in range(len(s)):
            while s[j] in chars:
                chars.remove(s[i])
                i+=1
            chars.add(s[j])
            maxstr =max(maxstr, j-i+1)
        return maxstr
def main():
    s="abcabcabcdaabb"
    o=Solution()
    print(o.lengthOfLongestSubstring(s))


if __name__ == "__main__":
    main()