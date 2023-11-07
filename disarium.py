num=int(input("enter the number"))
b=num
x=num
count=0
while b>0:
    b=b//10
    count=count+1
sum=0
while x>0:
    rem=x%10
    sum=sum+rem**count
    x=x//10
    count=count-1
if sum==num:
    print(sum,"the disarium number")
else:
    print("flase")
