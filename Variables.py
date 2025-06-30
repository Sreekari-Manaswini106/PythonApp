a, b, c = 10, 20, 30
d = e = f = 50 
print(a)
print(d)
print(b)
print(c)
a = int(input("Enter : "))
b = int(input("Enter : "))
print(a,b)
print(a+b)
print(a*b)
d,e = map(int,input("Enter d , e ").split()) # 10 20
print(d)
print(e)
age = int(input("Enter age : "))
if age>18:
    print("Eligible")
elif age==18:
    print("Can Vote")
else :
    print("Not Eligible")
n = int(input("pretty no : "))
if (n%10 == 7) or (n/10 == 7):
    print("Yes")
else :
    print("No")  

for i in range(5):
    print(i , "\t") 
    print(i,end = " ")
for i in range(10, 100):
    if(i %10==7) or (i//10 == 7):
        print(i, "\t")

# comprehensive list
list1 = [10,20,30,40,50]
print(sum(list1))
n = 10
list1 = []
for i in range(n):
    if i % 2 ==0:
        list1.append(i)
print(list1)
list2 =[x for x in range(n) if x%2 ==1]
print(list2)
