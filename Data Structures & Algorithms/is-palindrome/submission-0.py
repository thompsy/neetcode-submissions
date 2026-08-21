class Solution:
    def isPalindrome(self, s: str) -> bool:

        valid_chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        # Approach here is to have two pointers, one from the start and 
        # one from the end. Walk the string, skipping rejected characters
        # and comparing valid ones
        start: int = 0
        end: int = len(s) - 1

        s = s.lower()

        while start <= end:
            if s[start] not in valid_chars:
                start += 1
                continue
            if s[end] not in valid_chars:
                end -= 1
                continue

            print(f"{start}, {end}: {s[start]}, {s[end]}\n")
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

        