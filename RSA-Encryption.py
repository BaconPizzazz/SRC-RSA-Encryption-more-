import math

def størstefællesdivisor():
    a = int(input("indsæt første værdi: "))
    b = int(input("indsæt anden værdi: "))
    if a <= b - 1:
        temp = a
        a = b
        b = temp
    r = a%b 
    q = int(a%b)
    while (r!=0):
        a = b 
        b = r 
        q = int(a/b)
        r = a - (b * q) 
    print(b) 

størstefællesdivisor() 

        
