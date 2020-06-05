def shortenPath(path):
  hasSlash = path[0] == '/'
  new = []
  first = 0
  for last in range(0, len(path)):
    if path[last] == '/' or last == len(path)-1:
      substring = path[first:last] if path[last] == '/' else path[first:]
      if substring == '..':
        if len(new) > 0 and new[-1] != '..':
          new.pop()
        elif not hasSlash:
          new.append(substring)
      elif first != last and substring != '.':
        new.append(substring)
      first = last+1
  if hasSlash and len(new):
    new.insert(0, '')
  return '/'.join(new) if len(new) else '/'