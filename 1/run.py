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


cal2i = []
for i,CAL in enumerate(CAL2i):
    cal2i.append( [i,sum(CAL)] )

cal2i.sort( key=lambda ixcal: ixcal[1] )
v = sum( [ c for i,c in cal2i[-3:] ] )
print(v)
