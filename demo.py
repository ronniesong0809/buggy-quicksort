def partition (a, n):
    pivot = a[0]
    print("path: 1", end ="->")
    left = 0
    print("2", end ="->")
    right = n-1
    print("3", end ="->")
    while left < right:
        print("4", end ="->")
        while (a[right] >= pivot):
            print("5", end ="->")
            right-=1
            print("6", end ="->")
        print("5", end ="->")
        if (left != right):
            print("7", end ="->")
            a[left] = a[right]
            print("8", end ="->")
            left+=1
            print("9", end ="->")
        
        while (a[left] < pivot):
            print("10", end ="->")
            left+=1
            print("11", end ="->")
        print("10", end ="->")
        if (left != right):
            print("12", end ="->")
            a[right] = a[left]
            print("13", end ="->")
            right -= 1
            print("14", end ="->")
    print("4", end ="->")
    a[left] = pivot 
    print("15", end ="->")

if __name__ == "__main__":
    a = [3,1,2,3]
    n = 4
    print("a[]: ", a, ", n: ", n)
    partition(a, n)
    print("end\na[]:", a)
