a = list(map(int, input().split()))
def program(a):
    if a[0] == 1:
        for i in range(1, 9):
            if i != a[i-1]:
                return print("mixed")
        return print("ascending")
    elif a[0] == 8:
        for i in range(1, 9):
            if 9-i != a[i-1]:
                return print("mixed")
        return print("descending")
    else:
        print("mixed")
program(a)
    
    
