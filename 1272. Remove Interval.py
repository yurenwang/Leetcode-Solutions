class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        # The solution explains very well. 
        # We loop through the intervals once. First we find out if the current interval is overlapping with the toBeRemoved, then,
        #   if no overlap, we put it in result list, if there is overlap, we have 4 different kinds of overlaps, but they can all be
        #   represented as the part before the interval, plus the part after the interval. 
        
        # Time: O(N)  Space: O(N)
        
        res = []
        
        for interval in intervals:
            # if no overlap, then insert to result
            if not (toBeRemoved[0] < interval[1] and toBeRemoved[1] > interval[0]):
                res.append(interval)
            else:   # overlap
                if (interval[0] < toBeRemoved[0]):
                    res.append([interval[0], toBeRemoved[0]])
                if (toBeRemoved[1] < interval[1]):
                    res.append([toBeRemoved[1], interval[1]])
            
        return res