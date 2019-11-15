class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        str1 = ''.join(map(str, A))
        int1 = int(str1)
        int1 += 1
        l1 = [int(x) for x in str(int1)]
        return l1
