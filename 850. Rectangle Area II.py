class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # Line sweep
        # Imagine we have a horizontal line starting from the x axis, and moving upward. For each line at height y, we
        #   calculate the total width of covered area, and add it to the result. For each rectangle that has y1 and y2,
        #   we know that it starts at line y1 and ends at line y2, so for y1, we set it as START, and for y2, we set it
        #   as END. We add all rectangles to our list, each rectangle will be added twice, once when start, and once when
        #   end. When we meet START, we add the interval (x1, x2), when we meet END, we remove the interval (x1, x2).
        
        # Time: O(N*NlogN) because we loop N times when calculating the final result, and for each time, we need O(NlogN)
        #   time to sort and get the horizontal coverage
        # Space: O(N)
        
        START, END = 1, 0
        events = []     # this is the list of all start and end of rectangles
        
        # for each rectangle, add a start event, and an end event
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, START, x1, x2))  # start of the rectangle
            events.append((y2, END, x1, x2))    # end of the rectangle
        
        events.sort()
        active = []     # the current active (x1, x2) pairs that make up to the current horizontal coverage
        
        # the helper function to find total coverage at current horizontal line
        # the logic here works because the active will always be sorted by x1
        # this will take O(NlogN) time
        def findHorizontalCoverage():
            active.sort()
            res = 0
            cur = -1
            for x1, x2 in active:
                cur = max(cur, x1)
                res += max(0, x2 - cur) # only add to the result the extra part of current interval
                cur = max(cur, x2)
            return res
                
        result = 0
        prev_y = events[0][0]   
                
        # loop through the events, and calculate the horizontal coverage at each horizontal line
        # this will loop O(N) time
        for y, is_start, x1, x2 in events:
            # calculate the area covered so far
            result += findHorizontalCoverage() * (y - prev_y)

            if is_start:    # append the interval if it is start
                active.append((x1, x2))
            else:           # remove the interval if it is end
                active.remove((x1, x2))
            prev_y = y      # update the prev y
        
        return result % (10**9 + 7)