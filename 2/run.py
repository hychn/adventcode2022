def list2file(filename):
    returnList = []
    with open(filename, 'r') as filehandle:
        for line in filehandle:
            line = line.rstrip('\n')
            returnList.append(line)
    return returnList



INPUT = list2file('input2')
INPUT = list2file('input')

#0:rock, 1:paper, 2:scic
rep = {'A':0, 'B':1, 'C':2, 'X':0, 'Y':1, 'Z':2, }
Srep = {'X':0, 'Y':3, 'Z':6}
Score_A ={0:1, 1:2, 2:3}
Score_AB = {}
Draw = {(0,0):3, (1,1):3, (2,2):3 }
Win =  {(0,1):6, (1,2):6, (2,0):6 }
Lose = {}
for AB,score in Win.items():
    a,b = AB
    Lose[(b,a)] = 0

Score_AB.update(Draw)
Score_AB.update(Win)
Score_AB.update(Lose)

score = 0
for line in INPUT:
    A,B = line.split(' ')
    A,B = rep[A], rep[B]
    score += Score_AB[(A,B)] + Score_A[B]

print(score)


#part2
B_AS = {}
for AB,score in Score_AB.items():
    A,B = AB
    B_AS[(A,score)] = B

print(B_AS)
score = 0
for line in INPUT:
    A,S = line.split(' ')
    A,S = rep[A], Srep[S]
    B = B_AS[(A,S)]

    score += S + Score_A[B]

print(score)


