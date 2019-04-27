import matplotlib.pyplot as plt
import numpy as np
import csv

c_size = []
sr = int(input("Super Round : "))
diff = int(input("Percentage Difference : "))
with open("data t and rd SR "+str(sr)+" "+str(diff)+".csv", 'r') as csvnew:
    read = csv.reader(csvnew)
    for line1 in read:
        if line1[2] != "C1":
            c_size.append(list(map(float, line1))[2])

ave = sum(c_size)/len(c_size)

# plt.hist(c_size, bins=30)
# plt.ylabel('Frequency')
# plt.savefig("cluster.png")
# plt.close()
# plt.show()

n, bins, patches = plt.hist(x=c_size, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Cluster Size')
plt.ylabel('Frequency')
plt.title('Graph Cluster Size')
maxfreq = n.max()
plt.text(40, maxfreq/2, 'Average Cluster ='+str('%.2f' % ave), fontsize=10)


# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
plt.savefig("cluster.png")
plt.close()
