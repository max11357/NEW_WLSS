import csv
def read():
    data_set = []
    for i in range(1,20):
        with open('place'+str(i)+'.csv', 'r', newline='') as csvnew:
            read = csv.reader(csvnew)
            for line in read:
                data_set.append(float(line[0]))
        with open('place.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(data_set)
        data_set = []
##    print(type(data_set[1][0]))
read()
