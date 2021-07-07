number = []
numbers = []
key = []
f = open("Students.txt","r")
line = f.readlines()
f.close
import re
digitals = re.compile(r'\d+', re.I)
for i in line:
    a = re.findall(digitals, i)
    number.append(a[0])
    number.append(a[1])
    e = number.pop(0)
    w = number.pop(0)
    ans = e+"-"+w
    numbers.append(ans)
    for u in range(0,6):
        q = line[u].split(",")
        key.append(q[0])
line1 = {key[0]: numbers[0],key[1]: numbers[1],key[2]:numbers[2],key[3]:numbers[3],key[4]:numbers[4],key[5]:numbers[5]}
Q1 = list (line1.values()) [list (line1.keys()).index ('John')]
print("Q1:",Q1,"\n")
Q2 = list (line1.keys()) [list (line1.values()).index ('110-153')]
print("Q2:",Q2,"\n")
line1["Wendy"] = "110-543"
print("Q3:",line1,"\n")
A = list (line1.keys()) [list (line1.values()).index ('109-432')]
del line1[A]
print("Q4:",line1,"\n")
print("Q5:",len(line1),"人","\n")
numbers.pop(-1)
numbers.append("110-543")
Q6 = sorted(numbers)
print("Q6:",Q6)

        

