class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for start, end in intervals:

            # Current interval is completely before newInterval
            if end < newInterval[0]:
                result.append([start, end])

            # Current interval is completely after newInterval
            elif start > newInterval[1]:
                result.append(newInterval)
                newInterval = [start, end]

            # Overlapping intervals
            else:
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)

        result.append(newInterval)

        return result

            