# Start Tuple
tuple=()
print(tuple)

tuple=(1,2,3,4,5,6)
print(tuple)

tuple=("somnath","akram","soyam")
print(tuple)

s=("python",90,89.7,True)
print(s)

s=("soma",90,"hake")
b=("chattrapati","Shivaji","Maharaj")
print(s+b)

b=("chattrapati","Shivaji","Maharaj")
print(b*3)

# membership opertors
s=("Chattrapati","Shivaji","Maharaj")
print("Chattrapati" in s)
print("Chattrapati" not in s)

#index and slicing
s=("python",90,89.7,True)
print(len(s))
print(s[0])
print(s[-1])
n=4 # n means number of elements in tuple
print(s[n-1])
print(s[-n])

#slicing
print(s[:3])
print(s[1:])
print(s[::-1])
print(s[::2])

#
s=("somnath","madhav","hake")
print(s.index("madhav"))

#take a int values put in tuple sum of values in that value 
# in tuple and using predefine function & user define any concept
s=(1,2,3,4,5)
print(sum(s))
sum=0
for k in s:
  sum=sum+k
print("total",sum)

#check condition in a tuple condition is n=5  & n%5==0
s=(12,34,45,56,67,45)
for n in s:
   if n%5==0:
    print(n,"the value is divide by 5")
   else:
    print("the value is not divisible by 5")


#crate a tuple elemnets are apple banana orange then check the banan is present in that tuple aur not 
s=("apple","banana","orange")
if "banana" in s:
    print("banana is present in tuple")
else:
  print("banana is not present in tuple")
#tuple are 1,2,3,1,1,2,4,5 then count the operands of elemnts 2 
s=(1,2,3,1,1,2,4,5)
print(s.count(2))
#create a tuple using user through input
s=tuple(input("enter the elements").split())
print(s)


