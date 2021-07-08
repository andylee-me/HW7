num1 = input("請輸入算式(用空格隔開):")
num = num1.split()
while num != "end":
    w = len(num)
    for i in range(0,w):
        i = 0
        w = len(num)
        if num[i] == "(":
            left = i
        if num[i] == ")":
            right = i
            if right - left == 2:
                num.pop(left)
                num.pop(right-1)
                break
            for i in range(left,right):
                if num[i] == "/":
                    ans = float(num[i-1]) / float(num[i+1])
                    num.pop(i-1)
                    num.pop(i-1)
                    num.pop(i-1)
                    num.insert(i-1,ans)
                    w = len(num)
                    right -= 2
                    break
            for i in range(left,right):
                if num[i] == "x" or num[i] == "X":
                    num[i] = "*"
                if num[i] == "*":
                    ans = float(num[i+1]) * float(num[i-1])
                    ans = str(ans)
                    num.pop(i-1)
                    num.pop(i-1)
                    num.pop(i-1)
                    num.insert(i-1,ans)
                    i = 0
                    w = len(num)
                    right -= 2
                    break
            for i in range(left,right):
                if num[i] == "*" or num[i] == "/":
                    break
                if num[i] == "+":
                    ans = float(num[i+1]) + float(num[i-1])
                    ans = str(ans)
                    num.pop(i-1)
                    num.pop(i-1)
                    num.pop(i-1)
                    num.insert(i-1,ans)
                    i = 0
                    w = len(num)
                    right -= 2
                    break
            for i in range(left,right):
                if num[i] == "*" or num[i] == "/":
                    break
                if num[i] == "-":
                    ans = float(num[i-1]) - float(num[i+1])
                    ans = str(ans)
                    num.pop(i-1)
                    num.pop(i-1)
                    num.pop(i-1)
                    num.insert(i-1,ans)
                    i = 0
                    w = len(num)
                    right -= 2
                    break
    for i in range(0,w):
        if num[i] == "/":
            ans = float(num[i-1]) / float(num[i+1])
            num.pop(i-1)
            num.pop(i-1)
            num.pop(i-1)
            num.insert(i-1,ans)
            i = 0
            w = len(num)
            break
    for i in range(0,w):
        if num[i] == "x" or num[i] == "X":
            num[i] = "*"
        if num[i] == "*":
            ans = float(num[i+1]) * float(num[i-1])
            ans = str(ans)
            num.pop(i-1)
            num.pop(i-1)
            num.pop(i-1)
            num.insert(i-1,ans)
            i = 0
            w = len(num)
            break
    for i in range(0,w):
        for o in range(0,w):
            if num[i] == "+" and num[o] == "-":
                if i < o:
                    ans = float(num[i+1]) + float(num[i-1])
                    ans = str(ans)
                    num.pop(i-1)
                    num.pop(i-1)
                    num.pop(i-1)
                    num.insert(i-1,ans)
                    i = 0
                    w = len(num)
                    break
                else:
                    ans = float(num[o-1]) - float(num[o+1])
                    ans = str(ans)
                    num.pop(o-1)
                    num.pop(o-1)
                    num.pop(o-1)
                    num.insert(o-1,ans)
                    o = 0
                    w = len(num)
                    break
            elif len(num) <= 3:
                break
        if len(num)  <= 3:
            break
    for i in range(0,w):
        if num[i] == "*" or num[i] == "/":
            break
        if num[i] == "+":
            ans = float(num[i+1]) + float(num[i-1])
            ans = str(ans)
            num.pop(i-1)
            num.pop(i-1)
            num.pop(i-1)
            num.insert(i-1,ans)
            i = 0
            w = len(num)
            break
    for i in range(0,w):
        if num[i] == "*" or num[i] == "/":
            break
        if num[i] == "-":
            ans = float(num[i-1]) - float(num[i+1])
            ans = str(ans)
            num.pop(i-1)
            num.pop(i-1)
            num.pop(i-1)
            num.insert(i-1,ans)
            i = 0
            w = len(num)
            break
    answer = len(num)
    if answer == 1:
        print(num)
        answer == 0
        num1 = input("請輸入算式(用空格隔開):")
        num = num1.split()
print("結束程式")       
