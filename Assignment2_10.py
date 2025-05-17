def Addition(no1):
    sum =0
    result = len(str(no1))
    for i in range (result):
        ans = no1 % 10
        sum = sum + ans
        no1 = no1 // 10
    return sum
            

def main():
    print("Enter your Number :")
    value1 = int(input())
    
    result = Addition(value1)
    print("Addition of digit :",result)



if __name__ == "__main__":
    main()