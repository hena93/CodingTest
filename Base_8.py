'''
리스트와 내장함수(1)
'''
import random as r
a=[]
print(a)
b=list()
print(b)

a=[1, 2, 3, 4, 5]
print(a)
print(a[0])

b=list(range(1, 11))
print(b)

c=a+b
print(c) # 리스트 병합

print(a)
a.append(6) # 원소 추가
print(a)

a.insert(3, 7)  # 인덱스 3 위치에 7 추가
print(a)

a.pop() # 제일 큰 인덱스 데이터 제거
print(a)
a.pop(3) # 인덱스 3 데이터 제거

a.remove(4) # 값 4를 삭제
print(a)

print(a.index(5)) # 값 5의 인덱스 출력

a=list(range(1, 11))
print(a)
print(sum(a)) # 원소 전체 합
print(max(a)) # 리스트 내의 최대값
print(min(a)) # 리스트 내의 최소값
print(min(7, 5)) # 7과 5 중 더 작은 값 출력
print(min(7, 3, 5))
print(a)
r.shuffle(a) # 랜덤으로 섞기
print(a)
a.sort()
print(a)
a.sort(reverse=True)    # 내림차순
print(a)
a.clear()
print(a)
