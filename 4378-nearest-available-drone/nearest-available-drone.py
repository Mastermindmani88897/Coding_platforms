class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        tx, ty = target
        ans = -1
        min_dist = float('inf')

        for i, (x, y, r) in enumerate(drones):
            dist = abs(x - tx) + abs(y - ty)

            if dist <= r and dist < min_dist:
                min_dist = dist
                ans = i

        return ans