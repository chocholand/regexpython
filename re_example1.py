#-*- coding:UTF-8 -*-
import re
 
#re 모듈은 C확장 모듈이다.
#1)파이썬 에선 정규 표현식에 대한 인터페이스를 제공하여 주므로, RE를 객체로 컴파일해서 기능을 하용할 수 있다.
#정규표현식은 실체인 RegexObject로 컴파일된다.
#p = re.compile('ab*')
#print p
#group() 메서드는 정규식을 만족하는 string을 리턴
 
#정규표현식은 역사선 문자를 사용하여 특별한 의미를 요청하지 않고 문자를 쓰게 할 수 있다.
#1)역사선 문자를 사용하고 싶다면 역사선앞에 역사선을 그어야 한다.
#2)역사선 문자를 사용하고 싶다면 날 문자열 표기법인 r'abc'를 하면 된다.
#'\\\\abcd' ---> r'\\abcd'
 
#re모듈로 생성한 정규표현식 객체(RegexObject)를 사용하려면 파이썬에서 제공하는 메소드를 이용하면 된다.
#match() : 문자열의 처음에서 RE가 일치하는지 확인           없다면 return NONE
#match()는 찾고자 하는 문자열을 무조건 첫번째 인덱스부터 검색, 따라서 start()는 무조건 0.
#search() : 문자열을 훓어서, RE가 일치하는 위치를 찾는다      없다면 return NONE
#findall() : RE가 일치하는 곳의 모든 하부문자열을 찾아서, 그 문자열들을 리스트로 반환
#finditer(): RE가 일치하는 곳의 모든 하부문자열을 찾아서, 그 문자열들을 반복자로 반환
 
#match(),search() 성공했다면 MatchObject 반환
#MatchObject는 시작과 끝, 일치된 하부문자열 등의 정보
if __name__ == '__main__' :
    p = re.compile('[a-z]+')
    print p         #정규표현식 객체 (Regex Object)
    matchobj = p.match('abcd')
    print matchobj      #매칭 객체 (Match Object)
    print matchobj.span()   #문자열 시작과 끝점 오프셋 튜플로 반환
    matchobj = p.match('zzaba-a')
    print matchobj      #매칭 객체 (Match Object)
    print matchobj.span()
    matchobj = p.search('zzaba----abcde')   #문자열 전체를 훑는다
    print matchobj      #매칭 객체 (Match Object)
    print matchobj.span()
 
#findall() 성공했다면 일치된 문자열을 리스트로 반환
#finditer() 성공했다면 일치된 매칭객체를 반복자로 반환한다.
    str_list = p.findall('zzaba----abcde')  #문자열 전체를 훑는다. 일치하는 문자열 리스트
    print str_list      #문자열 리스트
 
    print 'finditer'
    matchobjs = p.finditer('zzaba----abcde')    #문자열 전체를 훑는다. 일치하는 MatchObject 반복자 반환
    for matchobj in matchobjs:  #일치하는 반복자들에서 값을 가져옴
        print matchobj      #MatchObject를 가져오게됨
        print matchobj.span()
        print matchobj.group()  #일치하는 문자열을 가져옴
    print 'finditer__end'
 
#MatchObject 의 메소드
#1)group() 일치된 문자열을 반환한다.
#2)start() 일치된 문자열의 시작 위치를 반환한다.
#3)end() 일치된 문자열의 끝 위치를 반환
#4)span 일치 위치를 (start, end)의 튜플로 반환

#findall()은 정규식에 해당하는 모든 문자열을 List 타입으로 리턴
#이것은 리턴값이 Match 오브젝트가 아님!!
#이 문제를 해결하기 위해서 finditer() 메서드를 이용, 
#iterator객체를 이용해서 Match 오브젝트를 순차적으로 리턴

