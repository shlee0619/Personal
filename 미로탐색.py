def move_position(n, plans):
    x, y = 1, 1
    # 방향 이동을 딕셔너리로 정의
    directions = {
        'L': (0, -1),
        'R': (0, 1),
        'U': (-1, 0),
        'D': (1, 0),
    }

    for plan in plans:
        if plan in directions:
            dx, dy = directions[plan]
            nx, ny = x + dx, y + dy
            # 공간을 벗어나는 경우 무시
            if 1 <= nx <= n and 1 <= ny <= n:
                x, y = nx, ny

    return x, y

# 사용자 입력 처리
if __name__ == "__main__":
    n = int(input("Grid size: "))
    plans = input("Plans (e.g., L R U D): ").split()
    final_position = move_position(n, plans)
    print("Final position:", final_position)