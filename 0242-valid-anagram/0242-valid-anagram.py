class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst = list(s)
        lst1 = list(t)
        lst.sort()
        lst1.sort()
        s = "".join(lst)
        t = "".join(lst1)
        if s == t:
            return True
        else:
            return False    



        