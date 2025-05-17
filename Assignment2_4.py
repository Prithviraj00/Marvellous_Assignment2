def Fact(no1):
    result = 0
    for i in range(1,no1):
        if no1 % i == 0:
            result = result + i
    return result
                           

def main():
    print("Enter your Number :")
    value1 = int(input())
    
    ans= Fact(value1)
    print ("Addition of Factors is :",ans)


if __name__ == "__main__":
    main()