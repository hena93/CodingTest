'''
문자열과 내장함수
'''
msg="It is Time"
print(msg.upper()) # 모두 대문자로 변경
print(msg.lower()) # 모두 소문자로 변경
tmp=msg.upper()
print(tmp)
print(tmp.find('T')) # T 문자가 존재하는 첫번째 인덱스
print(tmp.count('T')) # T문자가 몇개가 존재하는 지
print(msg[:2]) # 인덱스 0 ~ 1 까지 출력
print(msg[3:5]) # 인덱스 3 ~ 4 출력
print(len(msg)) # 문자열 길이

for i in range(len(msg)):
    print(msg[i], end='')
print()

for x in msg:
    print(x, end='')
print()

for x in msg:
    if x.isupper():
        print(x, end=' ')
print()

for x in msg:
    if x.islower():
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha(): # 알파벳인지 확인
        print(x, end=' ')
print()

tmp='AZ'
for x in tmp:
    print(ord(x)) # 아스키 넘버

tmp='az'
for x in tmp:
    print(ord(x)) # 아스키 넘버

tmp=65
print(chr(tmp))     # 아스키 넘버에 대응되는 문자

