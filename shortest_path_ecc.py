#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 21:46:59 2019

@author: yuxuanzhao
"""
import math
import matplotlib.pyplot as plt

#path = Shortest_path()
'''
check if a, b satisfied 4a^3+27b^2 mod p not equal to 0
'''
def notzero(a, b, p):
    if ((4*(a**3))+(27*(b**2)))%p == 0:
        return False
        #print("wrong")
    else:
        return True
        #print("right")

''' produce consecitive integers from -x to x
'''
def intGen(p):
    intlist = []
    begin = -((p-1)/2)
    end = (p-1)/2
    while int(begin)<=int(end):
        intlist.append(begin)
        begin = int(begin)+1
    return intlist

    #print(intlist)
    
    
'''put the consecutive x values in the ECC formula
get the y^2 value mod p, store the vlaue in a list
'''
def eccformula(a, b,p):
    #path = Shortest_path()
    y_sqr = 0
    y = 0
    y_list = []
    y_sqr_list = []
    for i in intGen(p):
        y_sqr =(i**3)+(a*i)+b
        #print(y_sqr)
        y_sqr_list.append(y_sqr)
    for j in y_sqr_list:
        y = j%p
        y_list.append(y)
        #print(y_list)
    return y_list

#print(eccformula(0,1,7))

'''Take the square of the consecitive integers from -x to x
take the mod and store the values in a list
'''
def intGen_sqr(p):
    #path = Shortest_path()
    intsqr = []
    mod_p = []
    sqr = 0
    for i in intGen(p):
        sqr = i**2
        intsqr.append(sqr)
    for j in intsqr:
        mod_p.append(j%p)
            #print(mod_p)
    return mod_p

        
def mergelist(list1, list2):
    merge_list = tuple(zip(list1, list2))
    return merge_list
        

def mergeecc(a,b,p):
    #path = Shortest_path()
    a = mergelist(intGen(p), eccformula(a,b,p))
    return a

def mergecon(p):
    #path = Shortest_path()
    b = mergelist(intGen(p), intGen_sqr(p))
    return b


'''check if the y^2 mod value generated by ecc in the 
integer sqre mod list
'''
def contains(a,b,p):
    #path = Shortest_path()
    num_pt = 0
    x_y_list = []
    #a = [x[1] for x in mergeecc(a, b, p)]
    #b = [y[1] for y in mergecon(p)]
    ecclist = mergeecc(a,b,p)
    intlist = mergecon(p)
    for (i,j) in ecclist:
        if any(n == j for (m,n) in intlist):
            x_y_list.append([i,j])
            num_pt = num_pt+2
    return x_y_list
'''
count and show the points in the plain, on the first region, going to imporve it soon
'''
def count_pt(a,b,p):
    #path = Shortest_path()
    num_pt = 0
    x_y_list = []
    #y_list = []
    #a = [x[1] for x in mergeecc(a, b, p)]
    #b = [y[1] for y in mergecon(p)]
    ecclist = mergeecc(a,b,p)
    intlist = mergecon(p)
    for (i,j) in ecclist:
        if any(n == j for (m,n) in intlist):
            x_y_list.append([i,j])
            if j == 0:
                num_pt = num_pt+1
            else:
                num_pt = num_pt+2
                #plt.scatter(zip(x_y_list))
    x_val = [x[0] for x in x_y_list]
    y_val = [x[1] for x in x_y_list]
    #print("the ECC list is", ecclist)
    #print("the INTEGER list is", intlist)
    #print(y_list)
    plt.scatter(x_val, y_val)
    #print(x_y_list)
    return num_pt
'''
find the distance between points and origin
'''
def distance(a,b,p):
    #path = Shortest_path()
    distance = []
    for x, y in contains(a,b,p):
        distance.append(math.sqrt((x**2)+(y**2)))
        #print(distance)
    return distance
print("The distance to the origin is",distance(0, 1, 7))
'''
find the shortest distance amoung the list of points
'''
def shortest_dis(a,b,p):
    #path = Shortest_path()
    if notzero(a,b,p) is False:
        return None
    else:
        return min(distance(a,b,p))

'''
firstly choose a prime p, then check from 0 to p, if satisfied in the 4a^3=27b^2 mod p
!= 0, then calculate all distances to origin from those points,
then find the smallest one, which is the clostest point. 
'''
def prime_p_closest(a,b,p):
    #path = Shortest_path()
    short_dis_list = []
    for i in range(p):
        #main(0,i,p)
        short_dis_list.append(shortest_dis(a, i, p))
        #print("the closest list is: ",short_dis_list)

    #print(short_dis_list)
    if None in short_dis_list:
        shortest = min(x for x in short_dis_list if x is not None)
    else:
        shortest = min(short_dis_list)

    #print("the shortest_dis_list is:", short_dis_list)
    #print("shortest distance is: ", shortest)


def short_dis_list(a,b,p):
    short_dis_list =[]
    for i in range(p):
        short_dis_list.append(shortest_dis(a, i, p))
    return short_dis_list

def list_dup_items(lis, item):
    #path = Shortest_path()
    start_at = -1
    locs = []
    while True:
        try:
            loc = lis.index(item, start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs
#source = short_dis_list(0,2,7)
#print("the index of value 1 is", list_dup_items(source, 1))



'''
change it soon, put the prime_p_closest into it. 
'''
def main(a,b,p):
    #path = Shortest_path()
    if notzero(a,b,p) is False:
        print("Your value is not satisfied")
    else:
        #prime_p_closest(a,b,p)
        #print("the consecutive int is", intGen(p))
        #print("eccformula", eccformula(a,b,p))
        #print("intGen_sqr",intGen_sqr(p))
        #print("the square of consecutive ints are", mergelist(intGen(p), intGen_sqr(p)))
        #print("tuplelist is ", mergelist(intGen(p), eccformula(a,b,p)))
        #print("contains",contains(a,b,p))
        #print("The distance is", distance(a,b,p))
        #print("The shortest distance with current b is", shortest_dis(a,b,p))
        #find the shortest diatnce amoung those points
        print("The number of points are:", count_pt(a,b,p))
        #print(prime_p_closest(a,b,p))
        #return shortest_dis(a,b,p)
        #print("the shortest distance is", shortest_dis(a,b,p))
        #since in our example, a is always 0
        compare_list = []
        for b in range(p):
            compare_list.append(shortest_dis(a, b, p))
            b = b+1
        #print("From b = 1 to p-1, the list of shortest value is", compare_list)
        #print("The b values are", list_dup_items(compare_list, 1), "have shortest path to the origin")
        
    
    

#prime_p_closest(1,1,7)
main(2,2,9)




    

        
    