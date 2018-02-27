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
user =[]

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
			user.append(row[0])
    # no_dupes = [x for n, x in enumerate(a) if x not in user[:n]]
    # print no_dupes
	for j in range(0, 2):
		userTest.append(time[j][0])
		ipTime = [0 for a in range(175)]
		for i in range(0, len(time) -1):
			if(time[i][0] == time[j][0]):
				index = ap.get(time[i][1])
				cur = (''.join(time[i])).split(' ')[-1].split(':')
				curTime = int(cur[0])*60*60 + int(cur[1])*60 + int(cur[2])
				ipTime[index] =  curTime
		print ipTime
		users.update({time[j][0]:ipTime})

	for k in range(0, 2):
		c=[]
		a = time[k][0]
		for z in range(k+1, 2):
			b = time[z][0]
			c=[users.get(a)[i] - users.get(b)[i] for i in range(len(users.get(a)))]
			c =  np.array(c)
			curMin = c.dot(np.transpose(c))
			minRes = curMin
		print minRes
# def buildheap(corUser):
# 	heapq.heapify(corUser)
# 	if len(heap) >= 5:  
# 	    top_item = heap[0] # smallest in heap  
# 	    if top_item < item: # min heap  
# 	      top_item = heapq.heappop(heap)  
# 	      print "pop", top_item,  
# 	      heapq.heappush(heap, item)  
# 	      print "push", item,  
#     else:
#     	heapq.heappush(heap, item)  
#     	print "push", item,  
 
# 	heap.sort()  

def main():
	convolution('fangte-vertices.csv', 'fangte-edges.csv')

if __name__ == '__main__':
    main()

