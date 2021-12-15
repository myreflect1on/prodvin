from collections import deque
with open(input(), encoding='utf-8') as f:
        print(*map(str.rstrip, list(deque(f, 10))), sep='\n')



