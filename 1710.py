class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda b: b[1], reverse=True)
        total_units = 0
        for count, units in boxTypes:
            if truckSize <= 0:
                break
            take = min(count, truckSize)
            total_units += take * units
            truckSize -= take
        return total_units
