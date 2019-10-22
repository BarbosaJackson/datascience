import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import shapiro as sh

def gen_v1(n, i):
	if(i < n//2):
		return 0
	elif(i == n//2):
		return 5
	else:
		return 5.1
def gen_v2(n, i):
	if(i < (n//2) - 2):
		return 1
	else:
		return 2

def generate(n, function_gen):
	data = []
	msum = 0
	for i in range(0, n):
		res = function_gen(n, i)
		msum += res
		data.append(res)
	outp = 'media = ' + str(round(msum / n, 2))
	print(outp)
	outp = 'mediana = '
	if(n & 1):
		outp += str(data[n//2])
	else:
		outp += str(round((data[(n//2) - 1] + data[n//2])//2, 2))
	print(outp)
	return data

def plotHist(data, bins, labels):
	plt.hist(data, bins, 1, labels)
	plt.show()

def checkNormalDistribuition(values):
	value = sh(values)
	return value[1] > 0.02

def printNormalDist(values, label):
	if(checkNormalDistribuition(values)):
		return label + " segue uma distribuição normal"
	else:
		return label + " nao segue uma distribuição normal"

def main():
	n = 100
	data_v1 = generate(n, gen_v1)
	print('-----------------------------')
	data_v2 = generate(n, gen_v2)
	bins = np.linspace(0, 6, 50)
	plotHist(data_v1, bins, 'V1')
	plotHist(data_v2, bins, 'V2')
	print(printNormalDist(data_v1, 'V1'))
	print(printNormalDist(data_v2, 'V2'))

main()