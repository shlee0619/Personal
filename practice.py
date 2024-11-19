class Stack:
    def __init__(self):
        # 스택을 저장할 리스트 초기화
        self.stack = []

    def push(self, item):
        # 스택에 요소를 추가
        self.stack.append(item)

    def pop(self):
        # 스택의 가장 위에 있는 요소를 제거하고 반환
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "스택이 비어 있습니다."

    def peek(self):
        # 스택의 가장 위에 있는 요소를 반환 (제거하지 않음)
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "스택이 비어 있습니다."

    def is_empty(self):
        # 스택이 비었는지 확인
        return len(self.stack) == 0

    def size(self):
        # 스택에 포함된 요소의 개수 반환
        return len(self.stack)

    def display(self):
        # 스택 상태를 출력
        print("스택 상태:", self.stack)

n = int(input("수열의 길이 n을 입력하세요 (1 ≤ n ≤ 100,000): "))

sequence = []
for _ in range(n):
    num = int(input())
    sequence.append(num)


stack = Stack()
# for idx, i in enumerate(sequence, start = 1):
#     stack.push(idx)
    

    

