import csv
def plot_data():
    data = []
    for i in range(2,10):
        t_predefine = i/10
        with open("data t 0.2and r0", 'r') as csvnew:
            read = csv.reader(csvnew)
            for line1 in read:
                data.append(list(map(int, line1)))
    print(data)
plot_data()
