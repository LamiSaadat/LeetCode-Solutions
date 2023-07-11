class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        digits_list = [int(x) for x in str(num)]
        for i in digits_list:
            if num % i == 0:
                count+=1
        return count

       