
#Created on Thu Sep 26 12:08:36 2018
#@author:Rutvi Desai


import math
import sys

# Extracting Data from data file

Datafile = sys.argv[1]
Datafile = open(Datafile, "r")
i = 0
data = []
ReadData = Datafile.readline()
while (ReadData != ""):
    a = ReadData.split()
    dataList = []
    for j in range(0, len(a), 1):
        dataList.append(float(a[j]))
    data.append(dataList)
    ReadData = Datafile.readline()

no_rows = len(data)
no_cols = len(data[0])
Datafile.close()


# calculating Labels from lable file
LabelFile = sys.argv[2]
LabelFile = open(LabelFile, "r")
Traininglabels = {}
ReadLabel = LabelFile.readline()
while (ReadLabel != ''):
    b = ReadLabel.split()
    Traininglabels[int(b[1])] = int(b[0])
    ReadLabel = LabelFile.readline()
LabelFile.close();

#finding the means

m0 = []
m1 = []
for i in range(0, no_cols, 1):
    m0.append(0)
    m1.append(0)

n0 = 0.0000001
n1 = 0.0000001

for i in range(0, no_rows, 1):
    if (Traininglabels.get(i) != None and Traininglabels.get(i) == 0):
        n0 += 1
        for j in range(0, no_cols, 1):
            m0[j] += data[i][j]
    if (Traininglabels.get(i) != None and Traininglabels.get(i) == 1):
        n1 += 1
        for j in range(0, no_cols, 1):
            m1[j] += data[i][j]
for j in range(0, no_cols, 1):
    m0[j] /= n0
    m1[j] /= n1

print("MeanMatrix: ")
print(m0)
print(m1)
    
    
#calculating Standard Deviations

VarMat0 = []
VarMat1 = []

for i in range(0, no_cols, 1):
    VarMat0.append(0.00000001)
    VarMat1.append(0.00000001)

for i in range(0, no_rows, 1):
    if (Traininglabels.get(i) != None and Traininglabels[i] == 0):
        for j in range(0, no_cols, 1):
            VarMat0[j] = VarMat0[j] + ((m0[j] - data[i][j]) ** 2)
    if (Traininglabels.get(i) != None and Traininglabels[i] == 1):
        for j in range(0, no_cols, 1):
            VarMat1[j] = VarMat1[j] + ((m1[j] - data[i][j]) ** 2)


for j in range(0, no_cols, 1):
    VarMat0[j] = VarMat0[j] / n0
    VarMat1[j] = VarMat1[j] /n1
print("")    
print("VarianceMatrix: ")
print(VarMat0)
print(VarMat1)
    
    

#Start Predicting

PredictedClass = {}
print("")
print("Class Prediction:")
for i in range(0, no_rows, 1):
    if (Traininglabels.get(i) == None):
        class0 = 0
        class1 = 0
        for j in range(0, no_cols, 1):
            class0 += (((m0[j] - data[i][j]) ** 2) / VarMat0[j])
            class1 += (((m1[j] - data[i][j]) ** 2) / VarMat1[j])
        if (class0 < class1):
            print("0", i)
            PredictedClass[i] = 0
        else:
            print("1", i)
            PredictedClass[i] = 1

