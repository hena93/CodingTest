'''
반복문(for, while)
'''
'''
a=range(10) # 0 ~ 9 정수리스트 생성
print(list(a))

for i in range(1, 11):
    print("hello")
    print(i)

for i in range(10, 0, -2):
    print(i)

'''

'''
i=1
while i<=10:
    print(i)
    i=i+1
    
i=10
while i>=1:
    print(i)
    i=i-1

i=1
while True:
    print(i)
    if i==10:
        break
    i+=1
'''

for i in range(1, 11):
    if i%2==0:
        continue
    print(i)

for i in range(1, 11):
    print(i)
    if i>15:
        break;
else:       # 정상적으로 종료되면 실행되는 else문
    print(11)
