from termcolor import colored
from PIL import Image, ImageDraw, ImageFont
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

def iteration():

    i,j = findNextTile()
    try:
        
        if(len(matrix[i][j]) == 3):
            outMatrix[i][j] = matrix[i][j][random.choices([0,1,2],weights = [100,20,40])[0]]
        elif(len(matrix[i][j])==2 and 'S' in matrix[i][j]):
            outMatrix[i][j] = matrix[i][j][random.choices([0,1],weights = [500,20])[0]]
        elif(len(matrix[i][j])==2 and 'L' in matrix[i][j]):
            outMatrix[i][j] = matrix[i][j][random.choices([0,1],weights = [20,50])[0]]
        elif(len(matrix[i][j])==1):
            outMatrix[i][j] = matrix[i][j][0]
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
            if(i-1>=0):
                matrix[i-1][j+1].remove('L')
        except:
            pass

        try:
            if(i-1>=0 and j-1>=0):
                matrix[i-1][j-1].remove('L')
        except:
            pass

        try:
            if(i-1>=0):
                matrix[i+1][j].remove('G')
        except:
            pass

        try:
            matrix[i+1][j+1].remove('S')
        except:
            pass

        try:
            if(j-1>0):
                matrix[i+1][j-1].remove('S')
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

#ДАЛЕЕ РАБОТА С ИЗОБРАЖЕНИЯМИ


def convert():
    imagesForConcat = []
    for i in range(N):
        imagesForConcat.append([])
        for j in range(N):
            if(outMatrix[i][j] == 'S'):
                imagesForConcat[i].append(Image.open('sky.png'))
            elif(outMatrix[i][j] == 'G'):
                imagesForConcat[i].append(Image.open('green.png'))
            elif(outMatrix[i][j] == 'L'):
                imagesForConcat[i].append(Image.open('land.png'))
    return imagesForConcat

def convertToImage():
    imagesForConcat = []
    for i in range(N):
        imagesForConcat.append([])
        for j in range(N):
            right = 0
            bottom = 0
            try:
                right = outMatrix[i][j+1]
            except:
                pass

            try:
                bottom = outMatrix[i+1][j]
            except:
                pass
            
            #Небо
            if(outMatrix[i][j] == 'S'):
                imagesForConcat[i].append(Image.open('models/sky.png'))

            #Дерево
            #elif(outMatrix[i][j] == 'G' and bottom == 'L' and outMatrix[i-1][j] == 'G'):
            #    imagesForConcat[i].append(Image.open('models/land1.png'))
            elif(outMatrix[i][j] == 'G' and right == 'S' and outMatrix[i][j-1] == 'S'):
                #outMatrix[i][j] = 'T'
                #imagesForConcat[i].append(Image.open('models/tree1.png'))
                imagesForConcat[i].append(Image.open('models/green-top.png'))
            #Угловые тайлы травы
            elif(outMatrix[i][j] == 'G' and (outMatrix[i-1][j] == 'S'or outMatrix[i-1][j] == 'T') and right =='S'):
                imagesForConcat[i].append(Image.open('models/green-top-right.png'))
            elif(outMatrix[i][j] == 'G' and (outMatrix[i-1][j] == 'S' or outMatrix[i-1][j] == 'T')and outMatrix[i][j-1] =='S'):
                imagesForConcat[i].append(Image.open('models/green-top-left1.png'))
            elif(outMatrix[i][j] == 'G' and right == 'G' and bottom == 'G'):
                imagesForConcat[i].append(Image.open('models/green-top-left1.png'))
            elif(outMatrix[i][j] == 'G' and outMatrix[i][j-1] == 'G' and bottom == 'G'):
                imagesForConcat[i].append(Image.open('models/green-top-right.png'))
            elif(outMatrix[i][j] == 'G' and outMatrix[i][j-1] == 'G' and outMatrix[i-1][j] == 'G'):
                imagesForConcat[i].append(Image.open('models/green-bottom-left.png'))
            elif(outMatrix[i][j] == 'G' and right == 'G' and outMatrix[i-1][j] == 'G'):
                imagesForConcat[i].append(Image.open('models/green-bottom-right.png'))

            #остальная трава
            elif(outMatrix[i][j] == 'G' and right == 'S'):
                imagesForConcat[i].append(Image.open('models/green-right.png'))
            elif(outMatrix[i][j] == 'G' and outMatrix[i][j-1] == 'S'):
                imagesForConcat[i].append(Image.open('models/green-left.png'))
            elif(outMatrix[i][j] == 'G' and outMatrix[i-1][j] == 'S'):
                imagesForConcat[i].append(Image.open('models/green-top.png'))

            #Земля
            elif(outMatrix[i][j] == 'L'):
                num = str(random.choices([1,2,3,4,5],weights = [1000,10,10,10,10])[0])
                filename = 'models/land'+str(num)+'.png'
                imagesForConcat[i].append(Image.open(filename))

            else:
                imagesForConcat[i].append(Image.open('models/land1.png'))
    return imagesForConcat
            

def sample():
    image = Image.new('RGBA', (10, 10))
    draw = ImageDraw.Draw(image)
    draw.rectangle(((0, 0), (10, 10)), fill=(82, 206, 0))  # синий квадрат
    image.save('green.png')

def concat(images):
    #for i in range(N):
    #    for j in range(N):
    #        images[i][j].load().convert('RGB')
    width, height = images[0][0].size  # size of element
    total_width = width * len(images[0])
    max_height = height * len(images)
    result = Image.new('RGBA', (total_width, max_height))  # common canvas


    y_offset = 0
    for line in images:
        x_offset = 0
        for element in line:
            result.paste(element, (x_offset, y_offset))
            x_offset += element.size[0]
        y_offset += line[0].size[1]
    
    result.save('result.png')

#img = Image.open('models/green-left.png')
#img.save('green1.png')
#Image._show('result.png')
#imgs = convertToImage()
concat(convertToImage())
#print(random.choices([1,2,3,4,5],weights = [100,10,10,10,10])[0])