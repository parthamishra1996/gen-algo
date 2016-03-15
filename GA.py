import sys
sys.path.append('/usr/lib/python2.7/dist-packages')
import numpy as np
import cv2
import Queue
import heapq
import math

#Function to get n bit binary representation of integer x
get_bin = lambda x, n: format(x, 'b').zfill(n)

nodes = int(input("Enter number of nodes: "))
#Size of encoding: size
size = int(math.ceil(math.log(nodes,2)))

map = {}

#Encoding of all the nodes into binary
print "Enter the co-ordinates(x y) for all the nodes"
for i in range(nodes):
	a = int(input("x: "))
	b = int(input("y: "))
	bin = get_bin(i,size)
	map[bin] = (a,b)

str_size = nodes*size
pop = int(input("Enter number of individuals in a population: "))

#Generate initial population


#Iterate till convergence
convergence = False
#while(!convergence):
	#calc_fitness(pop)
