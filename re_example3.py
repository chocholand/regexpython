#-*- coding:UTF-8 -*-
import re
#더많은 메타문자
#or 문자 apple또는 orange 어느 문자열과도 일치한다 , 기호문자 |에 일치시키려면 \나 문자 부류 안에 넣는다.
print '1.OR연산'
iter_= re.finditer(r'apple|orange', 'i like apple or orange')
for str_ in iter_:
    print str_.group()
 
#문자열의 마지막, 문자열의 마지막 NULL문자 전 이거나 마지막 \n 전에 위치할 때 인식
print '2-1.$끝문자'
iter_= re.finditer(r'}$', 'struct stu{char* name; int age}')
for str_ in iter_:
    print str_.group()
 
#$은 문자열의 마지막이거나 \n이 와야한다
print '2-2.$끝문자'
iter_= re.finditer(r'}$', 'struct stu{char* name; int age} void main(){ }\n')
for str_ in iter_:
    print str_.group()

 
#\b 단어 경계이다. 이는 0-너비 선언이다. 단어의 처음과 끝에만 일치한다.
print '3.\b문자'
iter_= re.finditer(r'\bint\b', 'struct stu{char* name;    int age} void main(){ }\n')
for str_ in iter_:
    print str_.group()
 
#그룹짓기 RE를 그룹 단위로 적용할 수 있다. 열린 그룹 순으로 매개변수로 1 ,2 ,3 을 넣으면 일치한 내용을 확인할 수 있다.
#구조체를 찾음
#\s 공백 \w영문자 []문자부류
print '4.그룹'
iter_= re.finditer(r'(struct\s\w*{([\w;,\s*]*)})', '  struct stu{char* name; int age} void main(){ }\n')
for str_ in iter_:
    print str_.group(0)
    print str_.group(1)
    print str_.group(2)
    print str_.groups()
 
#\1 \2 을 날 문자열에서 사용하면 () 와 같은 RE그룹을 역참조 할 수 있다.
#print '\60' 날을 붙이지 않을경우 아스키문자가 나타나게 된다.
#in in in 3번이 왜 1번만 RE에 일치하는것인가?
#in in 은 하나의 문자로 RE에 일치되었고 그다음 in은 짝지을 in 문자열이 없기 때문이다.
#\w 영문,숫자,언더바의 아무 한 문자와 매칭
#\s 스페이스 문자 한 문자와 매칭  
print '4.back-referenct'
iter_ = re.finditer(r'(\b\w+)\s+\1','Paris in the the in in in spring')
for str_ in iter_:
    print str_.group()
 
#이름 붙은 그룹 (?P<name>...) 을 통해 그룹에 이름을 지어줄 수 있다.
print '5.back-referenct name'
iter_ = re.finditer(r'(?P<reference>\b\w+)\s+\1','Paris in the the spring')
for str_ in iter_:
    print str_.group('reference')
#아래와 같은 형태로 활용 가능
"""
InternalDate = re.compile(r'INTERNALDATE "'
        r'(?P<day>[ 123][0-9])-(?P<mon>[A-Z][a-z][a-z])-'
    r'(?P<year>[0-9][0-9][0-9][0-9])'
        r' (?P<hour>[0-9][0-9]):(?P<min>[0-9][0-9]):(?P<sec>[0-9][0-9])'
        r' (?P<zonen>[-+])(?P<zoneh>[0-9][0-9])(?P<zonem>[0-9][0-9])'
        r'"')
"""

