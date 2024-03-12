n=eval(input("Enter a number"))
for i in range(1,n+1):
    cnt=0
    num=1
    while num<=i:
        r=i%num
        if r==0:
            cnt+=1
        num+=1
    if cnt==2:
        print("prime number",i)


#sum of odd and even numbers between any 2 numbers 
n=eval(input("Enter a lower number "))
q=eval(input("Enter a higher number "))
for i in range(n,q+1):   
    """se = 0
      so = 0
      while(i<q+1):
           if(i%2==0):
               se=se+i
               i+=1
           elif(i%2==1):
                 so=so+1
                 i+=1"""
print("sum of even numbers :",i)
print("sum of odd numbers :",i)
