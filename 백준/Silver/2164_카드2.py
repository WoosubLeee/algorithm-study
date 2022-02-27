N = int(input())
stack = list(range(1, N+1))
front, rear = -1, N-1

while rear - front > 1:
    front += 2
    if front == rear:
        break
    stack.append(stack[front])
    rear += 1
print(stack[rear])