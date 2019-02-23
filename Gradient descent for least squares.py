import sys
import random
import math

# Read Data

Datafile = sys.argv[1]
Datafile = open(Datafile, "r")
#Datafile = open("C:\\Users\Rutvi\Data.DATA")
data = []
i = 0
dr = Datafile.readline()

while(dr != '') : #read
    d1 = dr.split()
    d2 = len(d1)
    dr2 = []
    for j in range(0, d2, 1):
        dr2.append(float(d1[j]))
        if j == (d2-1) :
            dr2.append(float(1))
        #data.append(r2)

    data.append(dr2)
    dr = Datafile.readline()

no_rows = len(data)
no_cols = len(data[0])

Datafile.close()

# Read Labels

LabelFile = sys.argv[2]
LabelFile = open(LabelFile, "r")
#LabelFile = open('C:\\Users\Rutvi\Label.LABELS')
Traininglabels = {}
n = [0, 0]
dl = LabelFile.readline()
while (dl != ''):
    dl1 = dl.split()
    Traininglabels[dl1[1]] = int(dl1[0])
    if (Traininglabels[dl1[1]] == 0):
        Traininglabels[dl1[1]] = -1;
    dl = LabelFile.readline()

    n[int(dl1[0])] += 1

LabelFile.close()

#Initialize w 

w = []
for j in range(0, no_cols, 1):
    # print(random.random())
    w.append(random.uniform(-0.01,0.01))
    w[j]=(0.02 * random.uniform(0,1)) - 0.01


# Doc product 

def dot_product(w, data):
    dp = 0
    for i in range(0, no_cols, 1):
        dp = dp+ w[i]*float(data[i])
    return dp


# Gradient descent
# For ionosphere
eta = 0.0001
error = no_rows + 10
diff = 1
count = 0
while ((diff) > 0.0001):
    dell = []
    for m in range(0, no_cols, 1):
        dell.append(0)
    for j in range(0, no_rows, 1):
        if (Traininglabels.get(str(j)) != None):
            dp = dot_product(w, data[j])
            for k in range(0, no_cols, 1):
                dell[k] += (Traininglabels.get(str(j)) - dp) * data[j][k]


    for j in range(0, no_cols, 1):
        w[j] = w[j] + eta * dell[j]

    prev = error
    error = 0

    for j in range(0, no_rows, 1):
        if (Traininglabels.get(str(j)) != None):
             error += (Traininglabels.get(str(j)) - dot_product(w, data[j])) ** 2
            
    if (prev > error):
        diff = prev - error
    else:
        diff = error - prev
    count = count + 1
    
    
print ("error = " + str(error))


norm = 0
for i in range(0, (no_cols - 1), 1):
    norm += w[i] ** 2

norm = math.sqrt(norm)

print ("w ", w)
d_orgin = abs(w[len(w) - 1] / norm)

print ("Distance to origin = " + str(d_orgin))


#Calculate prediction 

print("Predicted Labels:")
for i in range(0, no_rows, 1):
    if (Traininglabels.get(str(i))==None):
        dp = dot_product(w, data[i])
        if (dp > 0):
            print("1 " + str(i))
        else:
            print("0 " + str(i))

