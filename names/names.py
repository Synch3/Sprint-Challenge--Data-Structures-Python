import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
namesarray = sorted(names_1)

def BST(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        middle = int((low+high)/2)
        pivot = arr[middle]
        if pivot > target:
            high = middle-1
        elif pivot < target:
            low = middle+1
        else:
            return pivot
    return -1


for name_2 in names_2:
    if BST(namesarray, name_2) is not -1:
        duplicates.append(name_2)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

