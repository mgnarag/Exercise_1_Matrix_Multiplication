import sys
import numpy as np

M1 = sys.argv[1]
M2 = sys.argv[2]


M1 = np.loadtxt(M1)
M2 = np.loadtxt(M2)


res = [[0 for x in range(2)] for y in range(2)]

for i in range(len(M1)):
	for j in range(len(M2[0])):
		for k in range(len(M2)):
			res[i][j] += M1[i][k]*M2[k][j]
print(res)


