def exexute_hcf(x,y):
    '''
    if x>y:
        smaller=y
    else:
        smaller=x

    for i in range(1,smaller+1):
        if (x%i==0) and (y%i==0):
            hcf=i
        
    return hcf
    '''
    while(y):
        x,y=y,x%y
    return x



x=int(input("Enter 1st  number "))
y=int(input("Enter 2nd numbe "))
print("The two number of hcf is ",exexute_hcf(x,y))

