def pattern(no1):
    for i in range (no1):
        print("* "*no1)
        
        

def main():
    print("Enter your Number :")
    value1 = int(input())
    
    pattern(value1)



if __name__ == "__main__":
    main()