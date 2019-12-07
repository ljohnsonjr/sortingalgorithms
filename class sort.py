import sys
import math
import random
class Counter:

    def __init__(self):
        self.compares = 1
        self.swaps = 1


def CreateRandomList(N):
    List = []
    for i in range(N):
        List.append(random.randrange(N))
    return List

def CreateMostlySortedList(N):
    List = CreateRandomList(N)
    List.sort()
    List[0],List[(len(List)-1)] = List[len(List)-1],List[0]
    return List


def bubblesort(A, C):
    somethingswitched = True
    while somethingswitched:
        somethingswitched = False
        for i in range(0, len(A) - 1):
            C.compares += 1
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                C.swaps += 1
                somethingswitched = True

def ShakerSort(A,C):
    somethingswitched = True
    while somethingswitched:
        somethingswitched = False
        for i in range(0, len(A) - 1):
            C.compares += 1
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                C.swaps += 1
                somethingswitched = True
        if somethingswitched == False:
            break
        somethingswitched = False
        for i in range(len(A) - 2, -1, -1):
            C.compares += 1
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                C.swaps += 1
                somethingswitched = True

    #https://www.youtube.com/watch?v=-zImXwDKuBk

def SelectionSort(A, C):
    for i in range(0, len(A) - 1):  # loops over all indexes
        C.compares += 1
        smallest_index = i
        for j in range(i + 1, len(A)):
            C.compares += 1
            if A[j] < A[smallest_index]:
                smallest_index = j
        if smallest_index != i:
            A[i], A[smallest_index] = A[smallest_index], A[i]
            C.swaps += 1

def MergeSort(A, C):
    if len(A) <= 1:
        return
    midpoint = int(len(A) / 2)
    Left = A[0:midpoint]
    Right = A[midpoint:len(A)]
    C.swaps += len(A)
    MergeSort(Left, C)
    MergeSort(Right, C)
    i = 0
    j = 0
    k = 0
    while i < len(Left) and j < len(Right):
        C.compares += 1
        if Left[i] <= Right[j]:
            A[k] = Left[i]
            C.swaps += 1
            i += 1
            k += 1
        else:
            A[k] = Right[j]
            C.swaps += 1
            j += 1
            k += 1
    while i < len(Left):
        C.compares += 1
        A[k] = Left[i]
        C.swaps += 1
        i += 1
        k += 1
    while j < len(Right):
        C.compares += 1
        A[k] = Right[j]
        C.swaps += 1
        j += 1
        k += 1

def quicksort(A, low, high, C):
    if (high - low) <= 0:
        return

    border = low + 1
    for i in range(border, high + 1):
        C.compares += 1
        if A[i] < A[low]:
            A[i], A[border] = A[border], A[i]
            C.swaps += 1
            border += 1
    pivot = border - 1
    A[low], A[pivot] = A[pivot], A[low]
    C.swaps += 1
    quicksort(A, low, pivot - 1, C)
    quicksort(A, pivot + 1, high, C)

def quicksortmodified(A, low, high, C):
    if (high - low) <= 0:
        return
    mid = (low + high) // 2
    A[mid], A[low] = A[low], A[mid]
    C.swaps += 1
    border = low + 1
    for i in range(border, high + 1):
        C.compares += 1
        if A[i] < A[low]:
            A[i], A[border] = A[border], A[i]
            C.swaps += 1
            border += 1
    pivot = border - 1
    A[low], A[pivot] = A[pivot], A[low]
    C.swaps += 1
    quicksortmodified(A, low, pivot - 1,C)
    quicksortmodified(A, pivot + 1, high,C)

def QuickSort(A, counts):
    quicksort(A, 0, len(A)-1, counts)

def MQuickSort(A, counts):
    quicksortmodified(A, 0, len(A)-1, counts)

def countingSort(A, C):
    C.compares = len(A)
    C.swaps = len(A)
    F = [0] * len(A)
    for value in A:
        F[value] += 1
    k = 0
    for i in range(len(F)):
        count = F[i]
        value = i
        for j in range(count):
            A[k] = value
            k += 1


def main():
    sys.setrecursionlimit(5000)
    sorts = [bubblesort,ShakerSort, SelectionSort, MergeSort, QuickSort, MQuickSort, countingSort]
    for size in range(3, 13):
        numItems = 2 ** size
        print("%10i" % (size), end="")
        for sort in sorts:
            A = CreateRandomList(numItems)
            C = Counter()
            sort(A, C)
            print("%10.2f" % (math.log(C.compares, 2)), end="")
        print()
    print()
    for size in range(3, 13):
        numItems = 2 ** size
        print("%10i" % (size), end="")
        for sort in sorts:
            A = CreateRandomList(numItems)
            C = Counter()
            sort(A, C)
            print("%10.2f" % (math.log(C.swaps, 2)), end="")
        print()
    print()
    for size in range(3, 13):
        numItems = 2 ** size
        print("%10i" % (size), end="")
        for sort in sorts:
            A = CreateMostlySortedList(numItems)
            C = Counter()
            sort(A, C)
            print("%10.2f" % (math.log(C.compares, 2)), end="")
        print()
    print()
    for size in range(3, 13):
        numItems = 2 ** size
        print("%10i" % (size), end="")
        for sort in sorts:
            A = CreateMostlySortedList(numItems)
            C = Counter()
            sort(A, C)
            print("%10.2f" % (math.log(C.swaps, 2)), end="")
        print()
    
if __name__ == '__main__':
    main()


