import math


def merge(list, p, q, r):
    L = list[p:q + 1]
    R = list[q + 1:r + 1]

    i, j = 0, 0
    for k in range(p, r + 1):
        if i == len(L):
            list[k:r + 1] = R[j:]
            break
        elif j == len(R):
            list[k:r + 1] = L[i:]
            break

        if L[i] <= R[j]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j += 1


def merge_sort(list, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(list, p, q)
        merge_sort(list, q + 1, r)
        merge(list, p, q, r)


list = [2, 4, 5, 7, 1, 2, 3, 6]
merge_sort(list, 0, len(list))
print(list)
