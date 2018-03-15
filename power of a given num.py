def power(base,exponential):
    if(exponential==1):
        return(base)
    if(exponential!=1):
        return(base*power(base,exponential-1))
base=int(input("Enter base: "))
exponential=int(input("Enter exponential value: "))
print("Result:",power(base,exponential))
