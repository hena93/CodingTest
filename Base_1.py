'''
변수명 정하기
1) 영문과 숫자, _로 이루어진다.
2) 대소문자를 구분한다.
3) 문자나 _로 시작한다.
4) 특수문자를 사용하면 안된다.(&, % 등)
5) 키워드를 사용하면 안된다. (if, for등)
'''
a=1
A=2
A1=3
#2b=4
_b=4
print(a, A, A1, _b)
a, b, c=3, 2, 1 # 동시에 3개 변수 생성 및 초기화
print(a, b, c)

# 값 교환
a, b=10, 20
print(a, b)
a, b=b, a
print(a, b)

# 변수 타입
a=12345 # 정수
print(a, type(a))
a=12.12345678 # 8바이트 실수
print(a, type(a))
a="student"
print(a, type(a))

#출력방식
print("student")
a, b, c=1, 2, 3
print(a, b, c)
print("number : ", a, b, c)
print(a, b, c, sep=', ') # sep : 변수 사이의 문자처리
print(a, b, c, sep='')
print(a, b, c, sep='\n')
print(a, end=' ')
print(b, end=' ')
print(c)
