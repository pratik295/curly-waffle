from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        def get_sort_by_unit(box):
            return box[1]

        boxTypes.sort(key=get_sort_by_unit, reverse=True)
        total = 0

        for box, unit in boxTypes:
            if truckSize >= box:
                total += unit * box
                truckSize -= box
            else:
                total += truckSize * unit
                break

        return total
