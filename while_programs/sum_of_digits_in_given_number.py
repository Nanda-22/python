n=eval(input("Enter a number")) 
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
print("Sum is ",s)