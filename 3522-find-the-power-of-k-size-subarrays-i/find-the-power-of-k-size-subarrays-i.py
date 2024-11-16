class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        result = [-1]* (length - k + 1)
        index_deque = collections.deque()

        for curr_index in range(length):
            if index_deque and index_deque[0] < curr_index -k +1:
                index_deque.popleft()
            if index_deque and nums[curr_index] != nums[curr_index -1]+1:
                index_deque.clear()
            
            index_deque.append(curr_index)

            if curr_index >=k-1:
                if len(index_deque) == k:
                    result[curr_index - k +1] = nums[index_deque[-1]]
                else:
                    result[curr_index - k + 1] = -1
            
        return result