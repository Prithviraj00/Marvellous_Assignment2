def Fact(no1):
    for i in range(no1):
        if (no1 == 1  or no1 == 0):
         return 1 
        else :
           return no1* Fact(no1-1)
                
                    

def main():
    print("Enter your Number :")
    value1 = int(input())
    
    ans= Fact(value1)
    print ("Factorial is :",ans)


if __name__ == "__main__":
    main()