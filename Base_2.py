'''
변수입력과 연산자
'''
#a=input("숫자를 입력하세요 : ")
#print(a)

'''
a, b=input("숫자를 입력하세요 : ").split() # 띄어쓰기로 구분
print(a, type(a))
c=a+b
print(c, type(c))
'''

'''
a, b=input("숫자를 입력하세요 : ").split()
a=int(a)
b=int(b)
print(a, b, type(a), type(b))
print(a+b)
'''

a, b=map(int, input("숫자를 입력하세요 : ").split())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) # 몫
print(a%b) # 나머지
print(a**b) # 거듭제곱

a=4.3
b=5
c=a+b
print(c, type(c))
