
class Solution(object):
	# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
  def numberOfSteps(self, num, times=0):
      """
      :type num: int
      :rtype: int
      """

      if num == 0:
      	return times

      if num % 2 != 0:
      	return self.numberOfSteps(num-1, times+1)
      else:
      	return self.numberOfSteps(num//2, times+1)
   


if __name__ == '__main__':
	s = Solution()
	print(s.numberOfSteps(14))

	print(s.numberOfSteps(8))

	print(s.numberOfSteps(123))

