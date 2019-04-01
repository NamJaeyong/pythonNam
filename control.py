number = 1
if number ==1:
    print('참참참')




number1 = 100
number2 = 200
number3 = 300
number4 = 400


a = number1 > number2
b = number3 < number4

if a:
    print('True')
else:
    print('False')

if a and b:
    print('True')
else:
    print('False')

list1 = ['a', 'b']
if 'a' in list1:
    print('a가 있읍니다.')
else:
    if 'b' in list1:
        print ('b가 있읍니다.')
    else:
        print('a와 b가 모두 없읍니다.')

if 'a' in list1:
    print('a가 있읍니다.')
elif 'b' in list1:
    print('b가 있읍니다.')
else:
    print('a와 b가 모두 없읍니다.')



list11 = ['a', 'b']

if 'a' in list11:
    pass
else:
    print('a가 없습니다.')

if 'a' in list11:
    print('있습니다.')
    print('진짜 있습니다.')
else:
    print('없습니다.')


if 'a' in list11: print('있습니다.'); print('진짜 있습니다.')
else: print('없습니다.')


treehit = 0
while treehit < 100:
    treehit = treehit + 1
    print("나무를 %d번 찍었습니다." %treehit)
    if treehit == 100:
        print("아부지~~나무 넘어가유~~~")

num1 = 0
while num1 < 10:
    num1 += 1
    print(num1)
    if num1 == 5:
        break
    

num2 = 0
while num2 < 10:
    num2 += 1
    if num2 % 2 == 0:
        continue
    print (num2)

n = 0
while n <4:
    n += 1
    print('*' * n )

list1111 = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]
for x in list1111:
    print(x)
    if x == 5:
        break

list22222 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in list22222:
    if x % 2 ==0:
        continue
    print(x)


a = range(0, 10)
print(a[9])
a = range(0, 10, 1)
print(a[9])
a = range(0, 10, 2)
print(a[1])




a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)

a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print (result)

a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)


a = 'mutzangesazachurum'
count = 0
for x in a:
    if x in 'aeiou':
        count += 1
print(count)    
