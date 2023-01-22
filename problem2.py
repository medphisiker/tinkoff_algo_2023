n = int(input())

# я решил избежать использования массива, для скорости и экономии места
i = 0
velocity_prev = int(input())
print(velocity_prev, end=' ')

while i < n - 1:
    velocity_cur = int(input())
    if velocity_cur > velocity_prev:
        velocity_cur = velocity_prev
    
    if i < n - 2:
        print(velocity_cur, end=' ')
    else:
        print(velocity_cur, end='')
        
    velocity_prev = velocity_cur
    i += 1
        
    