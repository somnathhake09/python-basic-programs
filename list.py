#task 1
s=[9,True,"somnath",3.14]
print(s)

#task2
s=[12,13,14,15,16]
print(len(s))

#task3
s=[1,2,3,4,5]
t=s*5
print(t)

#task4
s=[1,2,3,4,5,6,7]
t=[8,9,10,11,12]
print(s+t)

#create a empty list then assign a value and first value modify them
s=[]
b=[12,34,54,56]
b[0]=24
s=b
print(s)










# crate a  any list and them add a multiple element in that list
s=[12,23,34,45,67,78]
s.extend([45,56,65])
print(s)
#crate a any list and reverse them
s=[5,10,30,40,50]
s.reverse()
print(s)
#asume any list and delete  second postion element in that list
s=[89,88,68,2,36]
del s[1]
print(s)
# create a int list and shorted that list in accending order & decending order
s=[90,80,70,60,50]
s.sort() #accending
print(s)
s.sort(reverse=True) #decending
print(s)
# create a list and travel each element of a list
s=[20,40,60,80,100]
for i in s:
    print(i)
#create a list and reverse them using slice techniq
s=[1,2,3,4,5]
print(s[::-1])
# any list and delete last element of a list
s=[1,2,3,4,5]
s.pop(-1)
print(s)
