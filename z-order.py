

N, r, c = map(int, input().split())
def z_order(size, row, col, start):
    if size == 1:
        return start  
    
    
    half = size // 2
    if row < half and col < half:  
        return z_order(half, row, col, start)
    elif row < half and col >= half:  
        return z_order(half, row, col - half, start + half * half)
    elif row >= half and col < half:  
        return z_order(half, row - half, col, start + 2 * half * half)
    else:  
        return z_order(half, row - half, col - half, start + 3 * half * half)
    
size = 2**N
result = z_order(size, r, c, 0)
print(result)







    

