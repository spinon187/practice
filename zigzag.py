def convert(self, s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    arrays = [[] for n in range(numRows)]
    down = True
    row = 0
    for c in s:
        arrays[row].append(c)
        if down:
            row += 1
            if row == numRows - 1:
                down = False
        else:
            row -= 1
            if row == 0:
                down = True
    string = ''
    for i in arrays:
        string += ''.join(i)
    return string