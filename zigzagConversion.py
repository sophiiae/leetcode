class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1 or numRows >= len(s)):
            return s
        # initialize rows
        zigzag = ['' for row in range(numRows)]
        row, step = 0, 1
        for ch in s:
            zigzag[row] += ch
            if (row == 0):
                step = 1
            elif(row == numRows - 1):
                step = -1
            row += step
        return ''.join(zigzag)