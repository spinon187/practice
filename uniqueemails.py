# def numUniqueEmails(self, emails):
#     count = 0
#     uniques = {}
#     for a in emails:
#         name, domain = a.split('@')
#         filtered = []
#         for i in name:
#             if i == '+':
#                 break
#             elif i != '.':
#                 filtered.append(i)
#         final = ''.join(filtered) + '@' + domain
#         if final not in uniques:
#             count += 1
#             uniques[final] = True
#     return count

def numUniqueEmails(self, emails):
    count = 0
    uniques = set()
    for a in emails:
        name, domain = a.split('@')
        name = ''.join(name.split('+')[0].split('.'))
        full = name + '@' + domain
        uniques.add(full)
    return len(uniques)