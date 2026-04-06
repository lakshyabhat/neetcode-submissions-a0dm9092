class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startColor = image[sr][sc]

        self.dfs(image, sr ,sc, color, startColor)

        return image

    def dfs(self,self_image,r,c,color,startColor):
        row, col = len(self_image), len(self_image[0])
        if r < 0 or c<0 or r >= row or c >= col or self_image[r][c] != startColor or self_image[r][c] == color:
            return
        self_image[r][c] = color

        self.dfs(self_image,r+1,c,color,startColor)
        self.dfs(self_image,r-1,c,color,startColor)
        self.dfs(self_image,r,c+1,color,startColor)
        self.dfs(self_image,r,c-1,color,startColor)
