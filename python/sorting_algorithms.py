# Given array
arr = [5, 8, 16, 10, 3, 1, 4]

# 1. Bubble Sort
def bubble_sort(a):
    a = a.copy()
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# 2. Selection Sort
def selection_sort(a):
    a = a.copy()
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

# 3. Insertion Sort
def insertion_sort(a):
    a = a.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

# Run all
print("Original:", arr)
print("Bubble Sort:", bubble_sort(arr))
print("Selection Sort:", selection_sort(arr))
print("Insertion Sort:", insertion_sort(arr))
