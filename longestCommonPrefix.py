class Solution(object):
  def longestCommonPrefix(self, strs):
    # Longest Common Prefix    
    """
    :type strs: List[str]
    :rtype: str
    """

    if not strs:
      return ""

    if len(strs) == 1:
      return strs[0]

    temp_prefix = strs[0]

    for text in strs[1:]:
      
      temp_prefix = temp_prefix[:len(text)]
      for i, (temp_char, char) in enumerate(zip(temp_prefix, text)):

        if temp_char != char:
          temp_prefix = temp_prefix[:i]
          break


    return temp_prefix


class Solution2:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        return min(strs)

if __name__ == '__main__':
  s = Solution()
  s2 = Solution2()
  print(s.longestCommonPrefix(["flower","flow","flight"]))

  print(s.longestCommonPrefix(["dog","racecar","car"]))

  print(s.longestCommonPrefix(["aaa","aa","aaa"]))

  print(s.longestCommonPrefix(["caa","","a","acb"]))

  print(s.longestCommonPrefix(["","cbc","c","ca"]))

  print(s.longestCommonPrefix(["c","c"]))


  print(s2.longestCommonPrefix(["flower","flow","flight"]))

  print(s2.longestCommonPrefix(["dog","racecar","car"]))

  print(s2.longestCommonPrefix(["aaa","aa","aaa"]))

  print(s2.longestCommonPrefix(["caa","","a","acb"]))

  print(s2.longestCommonPrefix(["","cbc","c","ca"]))



