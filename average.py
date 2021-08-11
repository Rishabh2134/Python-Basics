total=0
count=0
a = list()
while True :
    inp = input("Enter a No. - ")
    if inp=='done' : break
    value=float(inp)
    a.append(value)
    total=total+value
    count=count+1

Average = total/count
print(Average)

average = sum(a)/len(a)
print("Average - ",average)
