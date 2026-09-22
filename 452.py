class Solution(object):
    def findMinArrowShots(self, points):
        if not points:
            return 0
        points.sort(key = lambda p: p[1])
        ar = 1
        arp = points[0][1]
        for s, e in points[1:]:
            if s > arp:
                ar += 1
                arp = e
        return ar
