import re

count = input('請輸入算式：');

while True:
    error = re.findall(r"[A-WY-Za-wy-z\u4e00-\u9fa5]+",count)
    if len(error) > 0:
        count = input('錯誤！請重新輸入算式：');
    else:
        break;
    

count = list(count)
chicken = ''.join(count)

for i in range(len(count)):
    if(count[i] == 'x'):
        count[i] = '*';
    elif(count[i] == '^'):
        count[i] = '**'

ans = ''.join(count)

print(chicken,'=',eval(ans))
