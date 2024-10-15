class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
  
        # Stack to keep track of counts of consecutive characters
        counts = []

        i = 0
        while i < len(s):
            # If this is the first character or it's different from the previous character
            if i == 0 or s[i] != s[i - 1]:
                counts.append(1)  # Start a new count
            else:
                # Increment the count for the current character
                counts[-1] += 1
                # If the count reaches k, pop the count and remove the substring
                if counts[-1] == k:
                    counts.pop()  # Remove the count
                    s = s[:i - k + 1] + s[i + 1:]  # Erase k characters
                    i = i - k  # Move the index back by k

            i += 1  # Move to the next character

        return s