import math


def binary_search(A, v, start, end):
    if start > end:
        return None
    mid = math.floor((start + end) / 2)
    if v == A[mid]:
        return mid
    elif v < A[mid]:
        return binary_search(A, v, start, mid - 1)
    elif v > A[mid]:
        return binary_search(A, v, mid + 1, end)


A = [12, 24, 32, 39, 45, 50, 54]
print(binary_search(A, 45, 0, len(A) - 1))
