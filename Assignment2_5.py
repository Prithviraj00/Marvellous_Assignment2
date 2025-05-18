def Prime(no1):
    primeno = True
    for i in range(2,no1):
        if no1 % i == 0:
            primeno = False
            print("It is not Prime")
            break
    if primeno :
        print ("It is prime number")
            
        

def main():
    print("Enter your Number :")
    value1 = int(input())
    
    Prime(value1)


if __name__ == "__main__":
    main()