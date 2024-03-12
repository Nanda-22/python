S = input("enter a string ")
def ishexadecimal(S):
    try:
        int(S, 16)
        return True
    except ValueError:
        return False

if ishexadecimal(S):
    print("Yes")
else:
    print("No")

def ishexadecimal(S):
    try:
        int(S, 16)
        return True
    except ValueError:
        return False
    
if (ishexadecimal(S)==True):
    print("valid")
else:
    print("not valid")
    
S1=S.split(":",5)
print(S1)

S.count(":")
