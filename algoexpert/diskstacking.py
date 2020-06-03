def diskStacking(disks):
	disks.sort(key=lambda x: x[2])
	maxes = [d[2] for d in disks]
	seq = [-1 for x in range(len(disks))]
	pointer = 0
	for i in range(len(disks)):
		for j in range(i):
			l1, l2 = disks[i][0], disks[j][0]
			w1, w2 = disks[i][1], disks[j][1]
			h1, h2 = disks[i][2], disks[j][2]
			if l1 > l2 and w1 > w2 and h1 > h2:
				if h1 + maxes[j] > maxes[i]:
					maxes[i] = h1 + maxes[j]
					seq[i] = j
			if maxes[i] > maxes[pointer]:
				pointer = i
	output = []
	while pointer >= 0:
		output.insert(0, disks[pointer])
		pointer = seq[pointer]
	return output