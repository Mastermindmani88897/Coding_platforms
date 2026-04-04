class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
        
        mat = []
        idx = 0
        for i in range(rows):
            mat.append(list(encodedText[idx:idx+cols]))
            idx += cols
        
        res = []
        
        for c in range(cols):
            i, j = 0, c
            while i < rows and j < cols:
                res.append(mat[i][j])
                i += 1
                j += 1
        
        return ''.join(res).rstrip()