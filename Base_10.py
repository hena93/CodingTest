'''
2차원 리스트 생성과 접근
'''
a=[0]*10 # 초기화 0으로 된 원소 10개 생성
print(a)

a=[[0]*3 for _ in range(3)] # _ : 변수없이 반복문만 실행
print(a)
a[0][1]=1
print(a)
a[1][1]=2
print(a)

for x in a: # 행으로 출력
    print(x)

for x in a:
    for y in x:
        print(y, end=' ')
    print()
