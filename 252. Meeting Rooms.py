class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sort by start time, then check each one if starts before prev end
        # Time: O(NlogN)  Space: O(1)  (actually O(N) because the sorting that Python use will take O(N) space)
        
        intervals.sort(key = lambda x : x[0])
        prev = -1
        
        for start, end in intervals:
            if start < prev:
                return False
            prev = end
        
        return True