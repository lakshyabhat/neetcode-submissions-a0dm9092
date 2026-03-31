class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l1, l2 = 0, 0
        while l1 < len(word) and l2 < len(abbr):
            if abbr[l2].isdigit():
                if abbr[l2] == '0':
                    return False
                prev_l2 = l2
                while l2 < len(abbr) and abbr[l2].isdigit():
                    l2 += 1
                l = int(abbr[prev_l2:l2])
                l1 += l
                continue
            if l2>=len(abbr) or l1>= len(word) or abbr[l2] != word[l1]:
                return False
            l2 += 1
            l1 += 1
        return len(word) == l1 and len(abbr) == l2
