class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # There are two ways to solve this problem
        #   1. The common way: Which is to sort the two lists first, then use two pointers p1 and p2 for slots1 and slots2,
        #       find overlap time if there is any, and move forward the pointer that point to an earlier end time, return
        #       result if the overlap time is greater than duration
        #   2. Use a min heap, and add all slots into the heap. Each time we pop from the heap and check if there is an
        #       overlap with the current slot. If there is an overlap, we know that the two slots are from different people,
        #       because in the question body, we know that time slots for a single person will never overlap
        
        # I will use the tradition way to solve this, which is to sort first then use two pointers.
        # Time: O(MlogM + NlogN) where M, N are length of two lists
        # Space: O(1)
        
        # Sort by start time, and set two pointers
        slots1.sort(key = lambda x : x[0])
        slots2.sort(key = lambda x : x[0])
        p1 = p2 = 0
        
        while p1 < len(slots1) and p2 < len(slots2):
            # calculate the overlap, overlap is the interval between the larger of the start, and the smaller of the end
            start, end = max(slots1[p1][0], slots2[p2][0]), min(slots1[p1][1], slots2[p2][1])
            # return if overlap is larger than duration
            if end - start >= duration:
                return [start, start + duration]
            # increase p1 or p2
            if slots1[p1][1] < slots2[p2][1]:
                p1 += 1
            else:
                p2 += 1
        
        return []
        