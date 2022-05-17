n  = input('cat de lung = ')
arr = []
nr_max = -1
temp = []
for _ in range(int(n)):
    arr.append(int(input(f'arr[{_}]: ')))

copy = arr[::]
copy.sort()
nr_max = copy[0]

print(nr_max)
print(arr)
    
for _ in arr[nr_max:]:
    temp.append(_)
    pass