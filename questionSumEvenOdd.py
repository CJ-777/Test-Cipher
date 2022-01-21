def sumEvenOdd(N):
    sumEven=0
    sumOdd=0
    for digit in N:
        digit=int(digit)
        if digit%2==0:
            sumEven+=digit
        else:
            sumOdd+=digit
    
    print(sumEven, sumOdd)
        
    
def main():
    n=input("Enter number : ").strip()
    sumEvenOdd(n)

main()