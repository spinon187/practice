def longestCommonSubsequence(str1, str2):
  matrix = [[[] for x in range(len(str2)+1)] for y in range(len(str1)+1)]
  for row in range(len(str1)):
    for col in range(len(str2)):
      left = matrix[row+1][col]
      top = matrix[row][col+1]
      diag = matrix[row][col]
      if str1[row] == str2[col]:
        matrix[row+1][col+1] = diag + [str1[row]]
      else:
        if len(left) < len(top):
          matrix[row+1][col+1] = top
        else:
          matrix[row+1][col+1] = left
  return matrix[-1][-1]