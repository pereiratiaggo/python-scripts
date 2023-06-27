import threading

def task1():
    x = 0
    while x < 20:
        print("Task 1")
        x += 1

def task2():
    x = 0
    while x < 20:
        print("Task 2")
        x += 1

threading.Thread(target=task1).start()
task2()