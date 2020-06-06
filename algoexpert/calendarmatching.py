def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
	cal1 = convertCalendar(calendar1, dailyBounds1)
	cal2 = convertCalendar(calendar2, dailyBounds2)
	flat = flatten(cal1, cal2)
	return findWindows(flat, meetingDuration)
	
	

def findWindows(cal, duration):
	windows = []
	for i in range(1, len(cal)):
		size = cal[i][0] - cal[i-1][1]
		if size >= duration:
			windows.append([cal[i-1][1], cal[i][0]])
	return list(map(lambda x: [convertMtoH(x[0]), convertMtoH(x[1])], windows))
	
def flatten(cal1, cal2):
	merged = []
	i, j = 0, 0
	while i < len(cal1) and j < len(cal2):
		if cal1[i] < cal2[j]:
			merged.append(cal1[i])
			i += 1
		else:
			merged.append(cal2[j])
			j += 1
	while i < len(cal1):
		merged.append(cal1[i])
		i += 1
	while j < len(cal2):
		merged.append(cal2[j])
		j += 1
	flat = [merged[0]]
	for x in range(1, len(merged)):
		prevStart, prevEnd = flat[-1][0], flat[-1][1]
		currStart, currEnd = merged[x][0], merged[x][1]
		if currStart <= prevEnd:
			flat[-1] = [prevStart, max(currEnd, prevEnd)]
		else:
			flat.append(merged[x])
	return flat

def convertCalendar(calendar, bounds):
	cal = calendar[:]
	cal.insert(0, ['0:00', bounds[0]])
	cal.append([bounds[1], '23:59'])
	return list(map(lambda t: [convertHtoM(t[0]), convertHtoM(t[1])], cal))

def convertHtoM(time):
	split = time.split(':')
	hours = int(split[0]) * 60
	minutes = int(split[1])
	return hours + minutes

def convertMtoH(time):
	hours = str(time // 60)
	mins = str(time % 60) if time % 60 > 9 else '0' + str(time%60)
	return hours + ':' + mins