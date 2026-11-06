
from collections import deque

stack = []

def push(element):
    stack.append(element)
    print("Елемент додано:", element)

def pop():
    if len(stack) == 0:
        print("Стек порожній")
    else:
        print("Видалено:", stack.pop())

def peek():
    if len(stack) == 0:
        print("Стек порожній")
    else:
        print("Верхній елемент:", stack[-1])


queue = deque()

def enqueue(element):
    queue.append(element)
    print("Елемент додано в чергу:", element)

def dequeue():
    if isempty():
        print("Черга порожня")
    else:
        print("Видалено з черги:", queue.popleft())

def isempty():
    return len(queue) == 0


print("  СТЕК  ")
push(10)
push(20)
push(30)
peek()
pop()
peek()

print("  ЧЕРГА  ")
enqueue(10)
enqueue(20)
enqueue(30)
dequeue()
print("Черга порожня:", isempty())
dequeue()
dequeue()
print("Черга порожня:", isempty())
