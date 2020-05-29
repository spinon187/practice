def spiralTraverse(array):
	op = []
	sR, eR = 0, len(array)-1
	sC, eC = 0, len(array[0])-1
	while sR <= eR and sC <= eC:
		for col in range(sC, eC+1):
			op.append(array[sR][col])
		for row in range(sR+1, eR+1):
			op.append(array[row][eC])
		for col in reversed(range(sC, eC)):
			if sR == eR:
				break
			op.append(array[eR][col])
		for row in reversed(range(sR+1, eR)):
			if sC == eC:
				break
			op.append(array[row][sC])
		sR += 1
		eR -= 1
		sC += 1
		eC -= 1
	return op