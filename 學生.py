stu = ["John","Mary","Amy","Nick","Candy","Leo"]
number = []
numbers = []
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
line1 = {"John": numbers[0],"Mary": numbers[1],"Amy":numbers[2],"Nick":numbers[3],"Candy":numbers[4],"Leo":numbers[5]}
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
print("Q6:",line1.values())
