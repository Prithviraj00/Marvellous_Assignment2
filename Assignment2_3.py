def Fact(no1):
    fact =1
    for i in range(1,no1):
        fact = fact * no1
        no1 = no1 - 1  
    return fact  
                    

def main():
    print("Enter your Number :")
    value1 = int(input())
    
    ans= Fact(value1)
    print ("Factorial is :",ans)


if __name__ == "__main__":
    main()