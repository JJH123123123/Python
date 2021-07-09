'''
주민등록번호 

901201-1111111
abcdef-1111111

이메일 주소 

nadocoding@gmail.com
nudocoding@gmail.com

차량주소
11가 1234
123가 1234

IP 주소
192,168.0.1
1000.2000.3000.4000
'''

import re 

###? why? ''' '''oct( ) 'ord(c)? 

# pattern
p = re.compile("ca.e") 
# . : 하나의 문자 
# ^ : 문자열의 시작
# $ : 끝

# m = p.match("good care")

def print_match(m):
    # m = p.match(str1)
    if m:
        print("m.group() : ", m.group()) # 매칭된 문자열
        print("m.string() : ", m.string) # 입력받은 문자열 / string은 변수기 때문에 괄호 X  
        print("m.start() :",m.start())   # 매칭되는 문자열이 입력받은 문자열에서의 처음 인덱스 
        print("m.end() :",m.end())       # 매칭되는 문자열이 입력받은 문자열에서의 마지막 인덱스 
        print("m.span() :",m.span())     # 매칭되는 문자열이 입력받은 문자열에서의 처음부터 마지막까지 인덱스
    else:
        print("매칭되지 않음")
            
# m = p.match('careless') # match : 주어진 문자열과 처음부터 일치하는지 확인
# print_match(m)
# m = p.search("good care") # search : 주어진 문자열 중에 일치하는 게 있는지 확인
# print_match(m)

# Lst = p.findall("careless good care cafe")
# print(Lst)

# 1. re.compile('원하는 정규식') 
# 2. m = p.match("비교할 문자열") : 주어진 문자열이 처음부터 일치하는지 확인 
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는 게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "list" 형태로 반환
# 원하는 형태 정규식 :
# . : 하나의 문자 > care, cafe, case, (O) | caffe (X)
# ^ (^de) : 문자열의 시작 > desk, destination (O) | fade (X)
# $ ($se): 끝 > case, base (O) | face (X)
# etc 

print(1)

