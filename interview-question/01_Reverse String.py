arr = ["h", "e", "l", "l", "o"]

# arr = arr[::-1]
i = 0
j = len(arr) - 1

while(i < j):
    arr[i], arr[j] = arr[j], arr[i]
    i +=1
    j -=1

print(arr)
