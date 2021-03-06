# 배열
def en_queue(item):
    global rear
    if is_full():
        print('Queue is full')
    else:
        rear += 1
        queue[rear] = item


def de_queue():
    global front
    if is_empty():
        print('Queue is empty')
    else:
        front += 1
        return queue[front]


def is_full():
    return rear == len(queue) - 1


def is_empty():
    return front == rear


n = 3
queue = [0]*n
front, rear = -1, -1

for i in range(1, 4):
    en_queue(i)
for i in range(3):
    print(de_queue())

# list
queue = []
for i in range(1, 4):
    queue.append(i)
for i in range(3):
    print(queue.pop(0))
