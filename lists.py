#Lab 2 Lists
import random
alist = []

# Append Method
for i in range (50):
    alist.append(i)
    print (i)
random.shuffle(alist)
print ("\n" , alist)

#other list functions will be tested here
print ("\n COPY METHOD \n")
print (alist.copy(), "\n")

print ("\n COUNT METHOD \n")
print (alist.count(24), "\n")

print ("\n INDEX METHOD \n")
index = alist.index(24)
print ("The index of 24 is: ", index, "\n")

print ("\n POP METHOD AND SORT METHOD \n")
print (alist.pop(index), "\n")
alist.sort()
print (alist, "\n")

print ("\n REMOVE METHOD \n")
print (alist.remove(23), "\n")
print (alist, "\n")

print ("\n REVERSE METHOD \n")
print (alist.reverse(), "\n")
print (alist, "\n")
