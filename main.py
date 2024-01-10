from collections import deque

def solution(array, k):
    d = deque(array)
    permutation = []
    while d:
        d.rotate(1-k)
        item = d.popleft()
        permutation.append(item)
    return permutation

soldiers = int(input("Write number of Soldiers: "))
arr = [s+1 for s in range(soldiers)]
k = int(input("Write number of Soldiers to be killed: "))
print(solution(arr, k))


