available = [3,3,2]
_max =[[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
allocation = [[0,1,0],[2,0,0],[3,0,0],[2,1,1],[0,0,2]]
need = []

def banker():
    for i in range(len(_max)):
        for j in range(len(_max[i])):
            need.append(_max[i][j]-allocation[i][j])
    
    return [need[i:i+3] for i in range(0, len(need), 3)]

need = banker()

#check if system is in safe state

def safe_state():
    work = available
    finish = [False,False,False,False,False]
    sequence = []
    while False in finish:
        for i in range(len(need)):
            # if (need[i][0] <= work[0] and need[i][1] <= work[1] and need[i][2] <= work[2]) and finish[i] == False:
            #     work[0] += allocation[i][0]
            #     work[1] += allocation[i][1]
            #     work[2] += allocation[i][2]
            #     finish[i] = True
            #     sequence.append(f"p{i+1}")
            for j in range(len(need[i])):
                if need[i][j] <= work[j] and finish[i] == False:
                    work[j] += allocation[i][j]
                    finish[i] = True
                    sequence.append(f"p{i+1}")
    return sequence

print(safe_state())


