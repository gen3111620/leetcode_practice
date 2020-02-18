class Solution(object):
	# https://leetcode.com/problems/palindrome-number/
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
        	return False

        original_x = x
        reverse = 0

        while x > 0:
        	reverse = reverse * 10 + x % 10
        	x //= 10

        return reverse == original_x





if __name__ == '__main__':
	s = Solution()
	print(s.isPalindrome(121))

	print(s.isPalindrome(-121))

	print(s.isPalindrome(2121))

	print(s.isPalindrome(23442))
