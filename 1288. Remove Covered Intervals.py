class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # First sort the intervals by the starting point. If two intervals have the same start point, longer interval first, because 
        #   we want to capture the possible covered intervals if two intervals starts at the same place.
        # Then, loop through the intervals, and for each interval that ends later than the prev interval, we know that it is not covered,
        #   and we add the result count, and set the prev to curr for next loop's usage
        # If a interval ends before the prev interval, then it is covered, we do nothing
        
        # Time: O(NlogN) because of the sorting     Space: O(N) because in Python, the sort function takes O(N) space
        
        count = 1
        intervals.sort(key = lambda x: (x[0], -x[1]))
        prev_r = intervals[0][1]
            
        for i in range(1, len(intervals)):
            curr_l, curr_r = intervals[i]
            if curr_r > prev_r:
                count += 1
                prev_r = curr_r
        
        return count
                