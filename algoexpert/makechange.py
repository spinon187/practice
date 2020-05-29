def numberOfWaysToMakeChange(n, denoms):
  ways = [0] * (n+1)
	ways[0] = 1
	for d in denoms:
		if d <= n:
			for i in range(1, n+1):
				if d <= i:
					ways[i] += ways[i - d]
	return ways[n]