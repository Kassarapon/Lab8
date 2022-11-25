def part(arr, low, high):
	pivotindex = piv = arr[high]

	i = low - 1

	for j in range(low, high):
		if arr[j] <= piv:
			i = i + 1
			(arr[i], arr[j]) = (arr[j], arr[i])
	(arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
	return i + 1

def quicks(arr, low, high):
	if low < high:
		p = part(arr, low, high)
		quicks(arr, low, p - 1)
		quicks(arr, p + 1, high)

def merges(arr):
    if len(arr) > 1:
        m = len(arr)//2
        l = arr[:m]
        r = arr[m:]
        merges(l)
        merges(r)

        i = j = x = 0

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                arr[x] = l[i]
                i += 1
            else:
                arr[x] = r[j]
                j += 1
            x += 1
        while j < len(r):
            arr[x] = r[j]
            j += 1
            x += 1
        while i < len(l):
            arr[x] = l[i]
            i += 1
            x += 1

arr = [29, 10, 14, 37, 14, 20, 7, 16, 12]
print(" array : ")
print(arr)

merges(arr)
print("\n mergesort : ")
print(arr)

scale = len(arr)
quicks(arr, 0, scale - 1)
print("\n quicksort : ")
print(arr)

