def list2file(filename):
    returnList = []
    with open(filename, 'r') as filehandle:
        for line in filehandle:
            line = line.rstrip('\n')
            returnList.append(line)
    return returnList



def set2raw(raw):
    a,b, = raw.split('-')
    return set( range( int(a),int(b)+1) )

INPUT = list2file('input')

count = 0
overlap = 0
for line in INPUT:
    A,B = line.split(',')
    A,B = set2raw(A), set2raw(B)
    if A.issubset(B) or B.issubset(A):
        count+=1
    if len( A.intersection(B) )>0:
        overlap+=1

print(count)
print(overlap)

