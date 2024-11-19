import sys


input = sys.stdin.read
data = input().split()


N = int(data[0])


numbers = list(map(int, data[1:]))

print(min(numbers), max(numbers))