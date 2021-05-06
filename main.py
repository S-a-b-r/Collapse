from termcolor import colored
import random

N = 20
matrix = []
outMatrix = []

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
                out += colored(str(outMatrix[i][j]),'green')+" "
            elif(outMatrix[i][j] == 'S'):
                out += colored(str(outMatrix[i][j]),'cyan') + " "
            elif(outMatrix[i][j] == 'L'):
                out += colored(str(outMatrix[i][j]),'yellow') + " "
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

def updateOutMatrix():
    for i in range(N):
        for j in range(N):
            if(len(matrix[i][j])==1):
                outMatrix[i][j] = matrix[i][j][0]
                matrix[i][j].pop()

def iteration():
    i,j = findNextTile()
    try:
        outMatrix[i][j] = matrix[i][j][random.randint(0,len(matrix[i][j])-1)]
    except:
        pass
    #Чистим активный элемент начальной матрицы
    for k in range(len(matrix[i][j])):
        matrix[i][j].pop()

    #Чистим остальные элементы матрицы
    #Если активный элемент стал Небом
    if(outMatrix[i][j] == 'S'):

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

        try:
            matrix[i+1][j].remove('S')
        except:
            pass

    
    #Если активный элемент стал Землей
    if(outMatrix[i][j] == 'L'):

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

printMatrix()