def list2file(filename):
    returnList = []
    with open(filename, 'r') as filehandle:
        for line in filehandle:
            line = line.rstrip('\n')
            returnList.append(line)
    return returnList



X = list2file('input')
CAL2i = [ [] ]
for line in X:
    if len(line)==0:
        CAL2i.append([])
    else:
        CAL2i[-1].append( int(line) )

MAXCAL = 0
MAXI = 0
for i,CAL in enumerate(CAL2i):
    if sum(CAL)>=MAXCAL:
        MAXCAL = sum(CAL)
        MAXI = i

print( MAXI, MAXCAL)

