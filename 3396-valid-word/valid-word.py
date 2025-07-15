class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)<3:
            return False
        if '@' in word or '#' in word or '$' in word:
            return False
        word=word.lower()
        vowels=set(('a','e','i','o','u'))
        v=False
        c=False
        digits=set(('1','2','3','4','5','6','7','8','9'))

        for ch in word:
            if ch in vowels:
                v=True
            if ch not in vowels and ch not in digits:
                c=True
            if c and v :
                return True
        return False


    