
from collections import deque
import argparse

parser = argparse.ArgumentParser(description="Takes two integers and returns the permutation of Josephus Problem.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("soldiers", help="Number of Soldiers")
parser.add_argument("k", help="Number of steps")
args = parser.parse_args()  
config = vars(args)
soldiers = int(config['soldiers'])
k = int(config['k'])

def solution(array, k):
    d = deque(array)
    permutation = []
    while d:
        d.rotate(1-k)
        item = d.popleft()
        permutation.append(item)
    return permutation

arr = [s+1 for s in range(soldiers)]
print(solution(arr, k))