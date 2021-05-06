from termcolor import colored
import random

N = 20
matrix = []
outMatrix = []
countS = 0
countG = 0
countL = 0

for i in range(N):
    matrix.append([])
    outMatrix.append([])
    for j in range(N):
        matrix[i].append(['S','G','L'])
        outMatrix[i].append('0')

def printMatrix():
    out = ""
    for i in range(N):
        for j in range(N):
            if(outMatrix[i][j] == 'G'):
                out += colored('G','green')+" "
            #elif(outMatrix[i][j] == '0'):
            #    out += colored('G','green')+" "
            elif(outMatrix[i][j] == 'S'):
                out += colored('S','cyan') + " "
            elif(outMatrix[i][j] == 'L'):
                out += colored('L','yellow') + " "
            else:
                out += colored(str(outMatrix[i][j]),'red')+ " "
            #out += str(outMatrix[i][j])+ " "
        out+="\n"
    print(out)

def printMatrix1():
    out = ""
    for i in range(N):
        for j in range(N):
            out += str(matrix[i][j])+" "
        out+="\n"
    print(out)

countItaration = 0

def findNextTile():
    global countItaration
    if(countItaration == 0):
        countItaration+=1
        #return int(N/2),0
        return random.randint(int(N/3), int(N-N/3)),random.randint(int(N/3), int(N-N/3))
    minVarTile = 4
    minI = 0
    minJ = 0
    for i in range(N):
        for j in range(N):
            if(len(matrix[i][j])<minVarTile and len(matrix[i][j])!= 0 and outMatrix[i][j]!='S' and outMatrix[i][j]!='G' and outMatrix[i][j]!='L'):
                minVarTile = len(matrix[i][j])
                minI = i
                minJ = j
    return minI,minJ

#def updateOutMatrix():
#    for i in range(N):
#        for j in range(N):
#            if(len(matrix[i][j])==1):
#                outMatrix[i][j] = matrix[i][j][0]
#                matrix[i][j].pop()



def iteration():

    global countS
    global countG
    global countL

    i,j = findNextTile()
    try:
        #if(len(matrix[i][j]) == 3):
        #    outMatrix[i][j] = random.choices(matrix[i][j], weights=[100,20,100])[0]
        #elif(len(matrix[i][j])== 1):
        #    outMatrix[i][j] == matrix[i][j][0][0]
        #elif('L' in matrix[i][j] and 'G' in matrix[i][j]):
        #    outMatrix[i][j] = random.choices(matrix[i][j], weights=[3,1000])[0]
        #elif('S' in matrix[i][j] and 'G' in matrix[i][j]):
        #    outMatrix[i][j] = random.choices(matrix[i][j], weights=[1000,3])[0]

        #w = 0
        #arr = []
        #for i in range(len(matrix[i][j])):
        #    arr.append(w)
        #    w+=1
        
        if(len(matrix[i][j]) == 3):
            outMatrix[i][j] = matrix[i][j][random.choices([0,1,2],weights = [40,20,40])[0]]
        elif(len(matrix[i][j])==2 and 'S' in matrix[i][j]):
            outMatrix[i][j] = matrix[i][j][random.choices([0,1],weights = [500,20])[0]]
        elif(len(matrix[i][j])==2 and 'L' in matrix[i][j]):
            outMatrix[i][j] = matrix[i][j][random.choices([0,1],weights = [20,40])[0]]
        elif(len(matrix[i][j])==1):
            outMatrix[i][j] = matrix[i][j][0]
        #outMatrix[i][j] = matrix[i][j][random.choices(arr,weights = [40,20,40])[0]]
        #outMatrix[i][j] = matrix[i][j][random.randint(0,len(matrix[i][j])-1)]
    except:
        pass
    #Чистим активный элемент начальной матрицы
    for k in range(len(matrix[i][j])):
        matrix[i][j].pop()

    #Чистим остальные элементы матрицы
    #Если активный элемент стал Небом
    if(outMatrix[i][j] == 'S'):
        countS+=1

        try:
            if(i-1>=0):
                matrix[i-1][j].remove('L')
        except:
            pass

        try:
            if(i-1>=0):
                matrix[i-1][j].remove('G')
        except:
            pass

        try:
            if(j-1>=0):
                matrix[i][j-1].remove('L')
        except:
            pass

        try:
            matrix[i][j+1].remove('L')
        except:
            pass

        try:
            matrix[i+1][j].remove('L')
        except:
            pass
    
    #Если активный элемент стал травой
    if(outMatrix[i][j] == 'G'):
        countG+=1
        
        try:
            if(i-1>=0):
                matrix[i-1][j].remove('G')
        except:
            pass

        try:
            if(i-1>=0):
                matrix[i-1][j].remove('L')
        except:
            pass

        #try:
        #    if(i-1>=0):
        #        matrix[i+1][j].remove('G')
        #except:
        #    pass

        try:
            matrix[i+1][j].remove('S')
        except:
            pass

    
    #Если активный элемент стал Землей
    if(outMatrix[i][j] == 'L'):
        countL+=1

        try:
            if(i-1>=0):
                matrix[i-1][j].remove('S')
        except:
            pass

        try:
            if(j-1>=0):
                matrix[i][j-1].remove('S')
        except:
            pass

        try:
            matrix[i][j+1].remove('S')
        except:
            pass

        try:
            matrix[i+1][j].remove('S')
        except:
            pass
        
        try:
            matrix[i+1][j].remove('G')
        except:
            pass
    
    #printMatrix()
    #printMatrix1()


for i in range(N):
    for j in range(N):
        iteration()
arr = [0,1,2]
#print(matrix[0][0][random.choices(arr,weights = [40,20,40])[0]])
printMatrix()
#printMatrix1()