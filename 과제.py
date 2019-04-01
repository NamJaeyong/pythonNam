#과제1-1

result = 0
for n in range(1, 1000):
    if n % 3 == 0 :
        result += n
print(result)

#과제1-2
i = 5
while True:
    i -= 1  
    if i < 1: break  
    print ('*' * i) 

#과제1-3
grade = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
result = 0
while grade:  
    human = grade.pop()  
    if human >= 50:  
        result += human

print(result)  


#과제 2-1

for i in range(1, 101):
    print(i)

#과제 2-2
gradelist = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in gradelist:
    total += score 
average = total / len(gradelist) 
print(average) 

#과제 2-3
a = [1, 2, 3, 4, 5]
result = [num * 3 for num in a if num % 2 == 1]
print(result)