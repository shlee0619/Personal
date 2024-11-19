
from collections import deque

def bfs_word(begin, target, words):
    if target not in words:
        return 0

    def can_transform(word1, word2):
        return sum(1 for a, b in zip(word1, word2) if a != b) == 1

    queue = deque([(begin, 0)])
    visited = set()

    while queue:
        current_word, steps = queue.popleft()
        if current_word == target:
            return steps
        
        for word in words:
            if word not in visited and can_transform(current_word, word):
                visited.add(word)
                queue.append((word, steps + 1))

    return 0


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(bfs_word(begin, target, words)) 
