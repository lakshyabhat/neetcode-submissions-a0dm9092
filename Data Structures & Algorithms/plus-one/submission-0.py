class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            digits[i] += carry
            if i == len(digits)-1 and digits[i]<9:
                return digits[:i] + [digits[i]]
            tmp = digits[i]%10
            carry = digits[i]//10
            digits[i] = tmp
        if carry == 0:
            return digits
        return [carry] + digits