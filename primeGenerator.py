def pg(m,n):
    for num in range(m,n+1):
        fact = 0
        for i in range(1,num+1):
            if num%i == 0:
                fact +=1
        if fact==2:
            print(num)
            
def main():
    x = []
    testCases = int(input())
    for i in range(0,testCases):
        x.append(list(map(int, input().split())))
    for each in x:
        pg(each[0],each[1])
        print()
        
if __name__ == "__main__":
    main()
