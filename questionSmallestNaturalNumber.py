def smallestNaturalNumber(li):
    for i in range(max(li)):
        if i+1 not in li:
            return (i+1)
    return (max(li)+1)
    
def main():
    n=int(input("Enter size : "))
    li=[]
    for i in range(n):
        li.append(int(input("Enter ele : ")))
    print(smallestNaturalNumber(li))

main()