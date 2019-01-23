import csv
def read():
    data_set = []
    count = 1
    at1, at2, at3, at4,at5,at6 = [],[],[],[],[],[]
    at7, at8, at9, at10,at11,at12 = [],[],[],[],[],[]
    at13, at14, at15, at16,at17,at18,at19 = [],[],[],[],[],[],[]
    with open('place.csv', 'r', newline='') as csvnew:
        read = csv.reader(csvnew)
        for line in read:
            eval('at%d'% (count)).append(line)
            count += 1
    for i in range(1,19):
        print(eval('at%d'% (i)))        
read()
