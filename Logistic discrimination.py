import sys
import random
import math

#Load and read the datafile

Datafilename = sys.argv[1]
f = open(Datafilename, 'r')
data = []
l = f.readline()
while (l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    l2.append(float(1))
    data.append(l2)
    l = f.readline()

rows = len(data)
cols = len(data[0])
f.close()

#######Load and read the label file##############

Labelfilename = sys.argv[2]
f = open(Labelfilename)
trainlabels = {}
n = [0, 0]
l = f.readline()
while (l != ''):
    a = l.split()
    trainlabels[a[1]] = int(a[0])
    if (trainlabels[a[1]] == 0):
        '''trainlabels[a[1]] = -1;'''
    l = f.readline()
    n[int(a[0])] += 1

f.close()

# initialize "w" 
w = []
for j in range(0, cols, 1):
    w.append(0.02 * random.random() - 0.01)

# Calculation of doc product 

def dot_product(a, b):
    dp = 0
    for i in range(0, cols, 1):
        dp += a[i] * b[i]
    return dp

############Gradient descent iteration ############
############For Climate change#####################

error = rows * 10
eta = 0.001
#eta = 0.01
diff = 1
count = 0
 
#for (eta == 0.001 or eta == 0.01):
#stopping_cond = 0.001

# for i in range(0, 500, 1):
while ((diff) >  0.001):
    dellf = [0] * cols
    for j in range(0, rows, 1):
        if (trainlabels.get(str(j)) != None):
            dp = dot_product(w, data[j])
            expo = (trainlabels.get(str(j))) - (1 / (1 + (math.exp(-1 * dp))))
            for k in range(0, cols, 1):
                dellf[k] += (expo) * data[j][k]

########  Update "w"  #############################

    for j in range(0, cols, 1):
        w[j] = w[j] + eta * dellf[j]

    prev = error
    error = 0

# Compute error

    for j in range(0, rows, 1):
        if (trainlabels.get(str(j)) != None):
            # print(dot_product(w,data[j]))
            error += math.log(1 + math.exp((-1 * (trainlabels.get(str(j)))) * (dot_product(w, data[j]))))
    diff = abs(prev - error)
    

print("w= ",w)
normw = 0
for i in range(0, (cols - 1), 1):
    normw += w[i] ** 2

normw = math.sqrt(normw)
print("||w||=" + str(normw))
d_orgin = (w[len(w) - 1] / normw)
print ("Distance to origin = " + str(d_orgin))

#Prediction calculation

for i in range(0, rows, 1):
    if (trainlabels.get(str(i)) == None):
        dp = dot_product(w, data[i])
        if (dp > 0):
            print("1 " + str(i))
        else:
            print("0 " + str(i))
