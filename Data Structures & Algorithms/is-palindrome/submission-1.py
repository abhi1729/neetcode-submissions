class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedtext = "".join([char for char in s if char.isalnum()])
        cleaned_text = cleanedtext.lower()
        length = len(cleaned_text) // 2
        i = 0
        j = len(cleaned_text)-1
        isPalindrome = True
        while i < j :
            if cleaned_text[i] == cleaned_text[j] :
                isPalindrome = True
            else :
                isPalindrome = False
            j-=1
            i+=1
        return isPalindrome

        