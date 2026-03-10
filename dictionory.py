#strt dict
s={"name":"somnath","Rollno":4844,"Course":"Bvoc(SD)"}
print(s)
print(s["name"])

#create a student data dictonary at least 10 key value pair store data in dictory 
stud={"name":"Somnath",
      "Rollno":4844,
      "Course":"Bvoc(SD)",
      "Class":"Ty",
      "Subject":"Python",
      "Enrollment Id":203040503920,
      "Address":"Pune",
      "Pincode":411027,
      "State":"Maharashtra"}
#access value using in keys in each student
for i in stud.values():
    print(i)
#add new key value pairs in that dict
s={"name":"somnath","Rollno":4844,"Course":"Bvoc(SD)"}
s["Pincode"]=411027
print(s)
#update the first key value of existing 
s["name"]="soyam" 
print(s)

#value delete the last key value pair 
del s["Pincode"]
print(s) 

#check key exist aur not
if "name" in s:
    print("its exist")
else:
    print("its not exist")
    

#get all keys values and items and print it 
for a in s.items():
    print(a)
# CREATE A NESTED DICT
m={"name":"somnath","Rollno":4844,"Course":{"Software Devlopment":"Angular","Web Devlopment":"React"}}
print(m)


#create user throght dict  
#s=dict(input("enter the key ").split())
#print(s)
#clear entire key values pairs in that dict
m={"name":"somnath","Rollno":4844,"Course":{"Software Devlopment":"Angular","Web Devlopment":"React"}}
print(m.clear())
#create a dict using pre define  function
s=dict(name="somnath",id=1234,course="BVOCTY")
print(s)
#create a dict and store a information of cars 
car={"car":"BMW","Model":"BMW M4","Engine":"V8 Eng","priace":"1.5Cr"}
print(car)
#uing a dict () 
car=dict(car="BMW",Model="BMW M4",Engine="V8 Eng",priace="1.5Cr")
print(car)