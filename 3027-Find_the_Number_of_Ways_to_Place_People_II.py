class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Coordinate compression
        xs = sorted(set(x for x, _ in points))
        ys = sorted(set(y for _, y in points))
        xmap = {x: i for i, x in enumerate(xs)}
        ymap = {y: i for i, y in enumerate(ys)}

        n, m = len(xs), len(ys)
        grid = [[0] * (m + 1) for _ in range(n + 1)]

        # Mark points on compressed grid
        for x, y in points:
            grid[xmap[x] + 1][ymap[y] + 1] += 1

        # Build 2D prefix sum
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                grid[i][j] += grid[i - 1][j] + grid[i][j - 1] - grid[i - 1][j - 1]

        ans = 0
        # Check each pair (Alice, Bob)
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                xa, ya = points[i]
                xb, yb = points[j]
                if xa <= xb and ya >= yb:
                    # rectangle boundaries in compressed coords
                    x1, y1 = xmap[xa] + 1, ymap[yb] + 1
                    x2, y2 = xmap[xb] + 1, ymap[ya] + 1
                    cnt = grid[x2][y2] - grid[x1 - 1][y2] - grid[x2][y1 - 1] + grid[x1 - 1][y1 - 1]
                    if cnt == 2:
                        ans += 1
        return ans