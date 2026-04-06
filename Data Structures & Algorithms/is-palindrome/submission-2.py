class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        front, rear = 0, len(s) - 1

        while front < rear:
            if s[front] != s[rear]:
                return False
            front += 1
            rear -= 1

        return True