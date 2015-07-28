import math
primes = {2,3,5,7,11,13}

def primechecker(number):
    global primes
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i  == 0:
            break
    else:
        print(number)
        primes.add(number)

def pg_range(m,n):
    global primes
    for num in range(m,n+1):
        if num == 1 or (num%2 == 0 and num > 2):
            continue
        elif num == 2:
            primes.add(2)
            print(num)
            continue
        elif num in primes:
            print(num)
            continue
        elif primechecker(num):
                continue
            
def main():
    x, testCases = [], int(input())
    for i in range(0,testCases):
        x.append(list(map(int, input().split())))
    for each in x:
        pg_range(each[0],each[1])
        print("\n")
        
if __name__ == "__main__":
    main()
