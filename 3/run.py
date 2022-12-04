def list2file(filename):
    returnList = []
    with open(filename, 'r') as filehandle:
        for line in filehandle:
            line = line.rstrip('\n')
            returnList.append(line)
    return returnList


import string


p2item = { item:p+1 for p,item in enumerate(string.ascii_letters) }

INPUT = list2file('input')

total = 0
for line in INPUT:
    split = len(line)//2
    A,B = line[:split], line[split:]

    common = None
    for a in A:
        if a in B:
            common = a;break
    total += p2item[common]


print(total)


# part 2
total = 0
INPUTITER = iter(INPUT)
for A in INPUTITER:
    B,C = next(INPUTITER), next(INPUTITER)
    badge = None
    for a in A:
        if a in B and a in C: badge = a
    total += p2item[badge]
print(total)
