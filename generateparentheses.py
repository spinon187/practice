def generateParenthesis(n):
    op = []
    stack = [('(', 1, 0)]
    while stack:
        p, left, right = stack.pop()
        if left - right < 0:
            continue
        if left == n and right == n:
            op.append(p)
        if left < n:
            stack.append((p+'(', left+1, right))
        if right < n:
            stack.append((p+')', left, right+1))
    return op