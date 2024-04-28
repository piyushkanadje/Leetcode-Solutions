class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left = 0
        ans = float('inf')
        card_index = collections.defaultdict(int)
        for right in range(len(cards)):
            if cards[right] in card_index:
                # Calculate the window size only if this card has been seen before
                window_size = right - card_index[cards[right]] + 1
                ans = min(ans, window_size)
                # If the smallest possible answer is found, return early
                if ans == 2:
                    return ans
            # Update the last index of the current card
            card_index[cards[right]] = right

        # If no such subarray is found, return -1
        return -1 if ans == float('inf') else ans