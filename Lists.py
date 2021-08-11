friends = ['Joseph','Glenn','Sally']
print(len(friends))
print(range(len(friends)))

print(range(4))


for i in range(len(friends)) :
    friend = friends[i]
    print('Hi',friend)

#Concatenation

a = [1,2,3]
b = [4,5,6]
c = a+b
print(c)

#Slicing

d = [10,20,30,40,50,60]
print(d[1:3])
print(d[:5])
print(d[1:])
print(d[:])

#append

College = list()
College.append('Rishabh')
College.append('Parth')
print(College)

#'In' Operator

print(20 in d)
print(100 not in d)

#'Sort' Operator

College.sort()
print(College)

#'max' 'min' 'sum'

print(max(d))
print(min(d))
print(sum(d))
print(sum(d)/len(d))
