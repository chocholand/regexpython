#-*- coding:UTF-8 -*-
import re
#RE객체는 split() 함수를 지원한다. 반환값으로  split()으로 나눠진 문자열 리스트를 반환한다.
regexobj = re.compile(r'(\s|[.])')
str_list = regexobj.split('My major is Computer Scien.ce')
print str_list
#RE객체는 sub()함수로 문자열 치환을 지원한다. 반환값으로 변환된 문자열을 반환한다.
p = re.compile('section{ ( [^}]* ) }', re.VERBOSE)
str_ = p.sub(r'subsection{\1}','section{First} section{second}')
print str_
#
def hexrepl(match):
    "Return the hex string for a decimal number"
    value = int(match.group())
    return hex(value)
p = re.compile(r'\d+')
str_ = p.sub(hexrepl, 'Call 65490 or printing, 49152 for user code.')
print str_
 
# *을 이용하면 탐욕적 탐색을 한다. 탐욕적 탐색이란 문자열의 가장 끝부분부터 일치하는것을 찾는 것이다.
# *? +? ?? 등의 비탐욕적 메타문자를 사용하라.
p = re.compile(r'{.*?}')
str_iter= p.finditer('struct abc{char* b } struct b{ int a }')
for str_ in str_iter:
    print str_.group()

