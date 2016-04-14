### CODE ####

import sys
sys.path.append('/usr/lib/python2.7/dist-packages')
import numpy as np
#import cv2
import Queue
import heapq
import math


#Function to get n bit binary representation of integer x
get_bin = lambda x, n: format(x, 'b').zfill(n)

#Function to real representation of a binary numer fed in the form of  a list
def get_real_list(x):
    real = 0
    for i in range(len(x)):
        real +=x[i]*2**(len(x)-i-1)
    return real

#Number of nodes or path points to be travelled: nodes
nodes = int(input("Enter number of nodes: "))

#Size of encoding of a single string representing a node: enc_size
enc_size = int(math.ceil(math.log(nodes,2)))

#Maps
map_1 = {}  #Maps binary to co-ordinates
map_2 = {}  #Maps nodenumbers to binary

#Encoding of all the nodes into binary
print "Enter the co-ordinates(x y) for all the nodes"
for i in range(nodes):
    print "node ("+str(i)+") : " 
    a = int(input("x: "))
    b = int(input("y: "))
    bin = get_bin(i,enc_size)
    map_1[bin] = (a,b)
    map_2[i] = bin

 #commneted the older code snippet for entering the starting and ending node
 #what is the use of separately entering a start and end node
 #when they are part of the nodes already entered       
                      
##Enter the starting and ending nodes
#print "For starting node:"
#startx = int(input("x: "))
#starty = int(input("y: "))
#start = (startx,starty)
#
#print "For ending node:"
#endx = int(input("x: "))
#endy = int(input("y: "))
#end = (endx,endy)

#New code snippet to enter starting and ending nodes
print "Nodes List \n"
print range(nodes)
print
print "Please enter only those nodes in the node list \n"

start = int(input("Enter the starting node : "))
end = int(input("Enter the ending node : "))
print
print 

#Enter the connectivity of the nodes

nodes_conn = {}

for i in range(nodes):
    a = map_1[get_bin(i , enc_size)]
    ch =int(input("Number of nodes connected to Node "+str(i)+" : ")) 
    print "Enter the nodes connected to Node "+str(i)+" : "
    #ch = "Y"
    nodes_conn[a] = [a]
    for ch in range(ch):
        temp = int(input("Enter the neighbouring node :"))
        temp = map_1[get_bin(temp , enc_size)]
        nodes_conn[a].append(temp)


#Write a code to find the number of loops in the map,sine the number of loops is equal to the number of obstacles
#Well number of nodes will also do the trick but then the program will take longer to converge        
       
#String and population size computation
print
str_size = nodes*enc_size #change this to no.of.obstacles * enc_size
pop_size = int(input("Enter number of individuals in a population: "))
print

#Generate initial population
pop = []


for i in range(pop_size):
    ind = []
    for x in range(len(map_2[start])):
        ind.append(int(map_2[start][x]))
    mid_size = str_size - 2*enc_size
    for j in range(mid_size/enc_size):
        while(1):
            node_allowed = list((np.random.choice([0,1], size=(enc_size,))))
            if (get_real_list(node_allowed)<nodes):
                break
        ind+=node_allowed 
    for x in range(len(map_2[end])):
        ind.append(int(map_2[end][x]))
    print "Ind"+str(i)+"  "+str(ind)
    pop.append(ind)
    #del ind[:]
print "Population: "
print pop
print
print
#Initial Fitnesss
fit = [0 for x in range(pop_size)]

#Calculating the fitness of the population

def calc_fitness(pop, fit):
	#Calculating the fitness of the populaton,calls another function that calculates the indivisual population
	#Assign fitness considering connectivity and euler distance between two nodes
	for i in range(pop_size):
	    fit[i] = calc_fitness_indivisual(pop[i])

def calc_fitness_indivisual(indi):
    #converting to a list of characters to make it simple
    for i in range(len(indi)):
        indi[i] = str(indi[i])
        
    total_dist = 0
    for i in range(len(indi)/enc_size -  1):
        current_node_coordinates = map_1["".join(indi[i*enc_size:((i+1)*enc_size)])]
        next_node_coordinates = map_1["".join(indi[((i+1)*enc_size):((i+2)*enc_size)])]
        if (next_node_coordinates in nodes_conn[current_node_coordinates]):
            temp_1 = current_node_coordinates
            temp_2 = next_node_coordinates
            dist = math.sqrt((temp_2[0] - temp_1[0])**2 + (temp_2[1] - temp_1[1])**2)
            total_dist +=dist
        else:
            return 0
    if(total_dist):
        indi_fit = 1/total_dist
        return indi_fit
    else:
        return 0
    	

##Dummy fitness function
def calc_fitness(pop, fit):
    '''Function to calculate fitness of each individual of population'''
    #Assign fitness considering connectivity and euler distance between two nodes
    for i in range(pop_size):
        fit[i]=i

##Iterate till convergence
convergence = False

#Priority Queue to decide the rank on the basis of fitness: pq
pq = []

calc_fitness(pop,fit)

#Arrange on the basis of fitness
for i in range(pop_size):
	heapq.heappush(pq,(-fit[i],pop[i]))

#One with highest fitness, automatically at the end of priority queue
ctr = 0
print "Generation "+str(ctr)+": "
best_sol = heapq.heappop(pq)
print "Best: "+str(best_sol)

while(not convergence):
    
    #Selection operation

    best_ind = best_sol[1] #Check for [1] in case of error
    print "Best_ind: "+str(best_ind)
    new_pop = []
    new_pop.append(best_ind)
    new_pop.append(best_ind)
    for x in range(pop_size-2):
        new_pop.append(heapq.heappop(pq)[1])
    print "Reject: "+ str(heapq.heappop(pq))
    print "New pop: "+str(new_pop)
    #heapq.heappush(pq,best_sol)

    #Cross-over operation
    cross_pop = []
    for x in range(pop_size):
        cross_pop.append(new_pop[x][:len(new_pop[x])/2]+new_pop[pop_size-x-1][len(new_pop[x])/2:])

    print "cross_pop: "+str(cross_pop)
    #Mutation Operation

    #Iterate
    ctr+=1
    print "Generation "+str(ctr)+": "
    calc_fitness(cross_pop,fit)
    #Arrange on the basis of fitness
    for i in range(pop_size):
        heapq.heappush(pq,(-fit[i],cross_pop[i]))
    best_sol = heapq.heappop(pq)
    print "Best: "+str(best_sol)
    #Dummy convergence
    #ctr+=1
    if(ctr == 5):
        convergence = True

#Solution: best fit individual
print
print
print "Final Solution: "
print best_ind
print

print "End"
