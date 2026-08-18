class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        original = image[sr][sc]
        if original == color:
            return image
        rows = len(image)
        cols = len(image[0])
        queue = deque([(sr, sc)])
        image[sr][sc] = color
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < rows and
                    0 <= nc < cols and
                    image[nr][nc] == original):
                    image[nr][nc] = color
                    queue.append((nr, nc))
        return image        
