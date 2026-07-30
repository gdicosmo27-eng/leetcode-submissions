class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        ROWS, COLS = len(image), len(image[0])

        visited = set()
        
        def dfs(image, sr, sc, color):
            if (sr, sc) in visited:
                return
            if sr < 0 or sc < 0 or sr == ROWS or sc == COLS or image[sr][sc] != original:
                return
            
            image[sr][sc] = color
            visited.add((sr, sc))

            dfs(image, sr + 1, sc, color)
            dfs(image, sr - 1, sc, color)
            dfs(image, sr, sc + 1, color)
            dfs(image, sr, sc - 1, color)

            return
        
        dfs(image, sr, sc, color)
        return image