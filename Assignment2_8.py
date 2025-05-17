def pattern(no1):
    for i in range (1,no1+1):     
            for j in range (1,i+1):
                print(j,end =" ")
            print()    
        
        

def main():
    print("Enter your Number :")
    value1 = int(input())
    
    pattern(value1)



if __name__ == "__main__":
    main()