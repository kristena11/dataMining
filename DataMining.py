from datetime import datetime


def getInputDescriptor():
    while True:
        inputFile = input('Enter name of input file name: ')
        try:
            fd = open(inputFile)
            return fd
        except:
            print('unable to open file' + inputFile)
            continue
    

def getDataList(fd, col):
    dataList = list()
    dataTuple = list()
    
    fd.seek(0,0)
    
    lines = fd.read().split('\n')
    
    for line in lines:
        dataList.append(line.split(','))
    
    for elem in dataList:
        dataTuple.append((elem[0], elem[col]))  
     
    dataTuple.pop(0)    
    return dataTuple
    

def averageData(data):
   
    avg = list()
    
    date = data[0][0].split('-')
    month = date[1]
    year = date[0]
    yearAndMonth = year + '-' + month
    sum = 0
    count = 0
    
    for elem in data:
        if yearAndMonth in elem[0]:
            sum = sum + float(elem[1])
            count = count + 1
        else:
            avg.append((month + ':' + year, sum/count)) 
            sum = float(elem[1])
            count = 1
            date = elem[0].split('-')
            month = date[1]
            year = date[0]
            yearAndMonth = year + '-' + month
      
    
    
    avg.append((month + ':' + year, sum/count))
    return avg
   
def outputAverage(filename, avg): 
    of = open(filename, 'w')
    for elem in avg:
        of.write('{:10}{:10.2f}'.format(elem[0], float(elem[1])))
    of.close()
    
def main():
    fd = getInputDescriptor()
    for i in range(1,7):
        dataTuple = getDataList(fd, i)
        avgTuple = averageData(dataTuple)
        outputAverage('data_' + str(i) + '.txt' , avgTuple)
   
    
main()