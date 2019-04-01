# # 한줄 주석 처리 입니다.

# """
# 여러 줄 주석 처리입니다.
# """


# # 블록을 잡으신 후 컨트롤 ?를 누르세요

# '''
# 1. 숫자형
# 정수 : 123. 0. -55
# 실수 : 123. 55. -33. 12
# 8진수 & 16진수는 생략
# '''

# # a = 15
# # print (a)

# # b = 15.03
# # print (b)

# c = 10
# d = 5
# print(c+d)
# print(c - d)
# print(c*d)
# print(c/d)
# print(c//d)
# print(c % d)

# '''
# 2. 문자형
# 문자형은 '' 혹은 ""으로 감싸서 표현합니다.
# '''

# str1 = 'hello'
# str2 = 'world'


# print (str1, str2)

# # 문자열 연산
# print (str1 + str2)
# print (str1 * 3)


# '''
# 이스케이프 문자
# \n == 앤터키
# \t == tab키
# \" == "큰 따옴표"
# \' == "작은 따옴표"
# \\ == \
# '''

# print

# #문자열 인덱싱
# text = "hello world"
# print(text[0])
# print(text[1])

# #문자열 슬라이싱
# print(text[0:5])

# '''
# 3. 불 자료형
# 참/거짓을 나타내는 자료형입니다.
# True와 False가 있습니다.
# '''

# a = True

# list1 = ['hello', 'python', 'java', 'c++', [1, 2, 3]]
# print(list1[0])
# print(list1[0:2])
# print(list1[4][0])


# list2 = [1, 2]
# list3 = [3, 4]
# print(list2 + list3)
# print(list3 * 3)


# listA = ['a', 'b', 'c']
# print(listA[0])
# listA[0] = 'change'
# print(listA[0])


# listB = ['a', 'b', 'c']
# del listB[0]
# print(listB)

# listC = ['a', 'b', 'c']
# listC.append('d')
# print(listC)

# lst = ['Life', 'is', 'too', 'short']
# str24 = " ".join(lst)
# print(str24)



 

dic1 = {'이름' : '남재용', '나이': '20', '학교' : '고려대학교'}
print(dic1)

print(dic1['이름'])
print(dic1['나이'])

keylist = list(dic1.keys())
print(keylist)
valuelist = list(dic1.values())
print(valuelist)

keyvalue = list(dic1.items())
print(keyvalue)




# list1 = ['1', '2', '3', '4', '5']
# print(list1)
# setnum = set(['1', '2', '3', '4', '5'])
# print(setnum)

# setNumber = set([1, 3, 4, 2, 5])
# setStr = set(['1', '2', '3', '4', '5'])
# setStr2 = set('Good Morning')

# print(setNumber)

setNum = set(['1', '2', '3', '4', '5'])
print(setNum)
list2 = list(setNum)
print(list2[1])
tuple1 = tuple(setNum)

