class Solution:
    def isPalindrome(self, s: str) -> bool:
        h=""
        for i in s:
            if i.isalnum():
                h += i
        if h.lower() == h[::-1].lower():
            return True
        else:
            return False
        

        