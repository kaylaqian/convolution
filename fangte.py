import csv
import numpy as np
import scipy.stats as stats
import heapq

users = {}
time = []
ap = {}
userTest = []
minResult = {}
corUser = []

def convolution(verticesFile, edgesFile):
	vf = open(verticesFile, 'r')
	index = 0
	for row in csv.reader(vf, delimiter = ','):
		if (row[1] == 'ap'):
			ap.update({row[0] : index})
			index = index+1
	sorted(ap.keys())
	ef = open(edgesFile, 'r')
	for row in csv.reader(ef, delimiter = ','):
		if(row[-1].split(' ')[0] == '2017-08-18'):
			time.append(row)
	for j in range(0, 100):
		userTest.append(time[j][0])
		ipTime = [0 for a in range(175)]
		for i in range(0, len(time) -1):
			index = ap.get(time[i][1])
			cur = (''.join(time[i])).split(' ')[-1].split(':')
			curTime = float(cur[0])*60*60 + float(cur[1])*60 + float(cur[2])
			ipTime[index] =  curTime
		users.update({time[j][0]:ipTime})

	for k in range(0, 100):
		a = time[k][0]
		for z in range(k, 100):
			b = time[z][0]
			curMin = np.convolve(users.get(a), users.get(b), 'same')
			minRes = curMin
	print minRes

def buildheap(corUser):
	heapq.heapify(corUser)
	if len(heap) >= 5:  
	    top_item = heap[0] # smallest in heap  
	    if top_item < item: # min heap  
	      top_item = heapq.heappop(heap)  
	      print "pop", top_item,  
	      heapq.heappush(heap, item)  
	      print "push", item,  
    else:
    	heapq.heappush(heap, item)  
    	print "push", item,  
 
	heap.sort()  

def main():
	convolution('fangte-vertices.csv', 'fangte-edges.csv')

if __name__ == '__main__':
    main()

