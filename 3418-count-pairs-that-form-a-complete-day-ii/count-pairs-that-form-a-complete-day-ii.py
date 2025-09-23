from collections import Counter

class Solution(object):
    def countCompleteDayPairs(self, hours):
        hours = [h % 24 for h in hours]  # reduce modulo 24
        count_map = Counter(hours)
        count = 0

        for h in count_map:
            if h == 0 or h == 12:
                # pairs with themselves
                count += count_map[h] * (count_map[h] - 1) // 2
            elif h < 12:
                count += count_map[h] * count_map.get(24 - h, 0)

        return count
