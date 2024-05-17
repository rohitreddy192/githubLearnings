arr = [32, 5, 21]

i = 0

j = len(arr) - 1


while(i<j):
    while(j>i and arr[j]%2==0):
        j -= 1
        
    if(arr[i]%2==0):
        arr[i], arr[j] = arr[j],arr[i]
    
    i += 1

print(arr)

