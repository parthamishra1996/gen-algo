import sys
sys.path.append('/usr/lib/python2.7/dist-packages')
import numpy as np
#import cv2
import Queue
import heapq
import math


#Function to get n bit binary representation of integer x
get_bin = lambda x, n: format(x, 'b').zfill(n)

#Number of nodes or path points to be travelled: nodes
nodes = int(input("Enter number of nodes: "))

#Size of encoding of a single string representing a node: enc_size
enc_size = int(math.ceil(math.log(nodes,2)))

#Map to map the co-ordinates to binary encoding
map = {}

#Encoding of all the nodes into binary
print "Enter the co-ordinates(x y) for all the nodes"
for i in range(nodes):
	a = int(input("x: "))
	b = int(input("y: "))
	bin = get_bin(i,enc_size)
	map[(a,b)] = bin

#Enter the starting and ending nodes
print "For starting node:"
startx = int(input("x: "))
starty = int(input("y: "))
start = (startx,starty)

print "For ending node:"
endx = int(input("x: "))
endy = int(input("y: "))
end = (endx,endy)

#Enter the connectivity of the nodes


#String and population size computation
str_size = nodes*enc_size
pop_size = int(input("Enter number of individuals in a population: "))

#Generate initial population
pop = []
for i in range(pop_size):
	pop.append(list((np.random.choice([0,1], size=(str_size,)))))
print pop
fit = [0 for x in range(pop_size)]

def calc_fitness(pop, fit):
	'''Function to calculate fitness of each individual of population'''
	#Assign fitness considering connectivity and euler distance between two nodes
	for i in range(pop_size):
		fit[i]=pop_size-i-1
	#fit[1]=10
	#print fit	

##Iterate till convergence
convergence = False

#Priority Queue to decide the rank on the basis of fitness: pq
pq = []

calc_fitness(pop,fit)

#Arrange on the basis of fitness
for i in range(pop_size):
	heapq.heappush(pq,(fit[i],pop[i]))

#One with highest fitness, automatically at the end of priority queue
best_sol = pq[pop_size-1]

while(not convergence):		
	#Selection operation
	
	heapq.heappop(pq)[0] #Check for [1] in case of error
	heapq.heappush(pq,best_sol)

	#Cross-over operation

	#Mutation Operation

#Solution: best fit individual
#print pq[0][1]
