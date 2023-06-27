import threading
import time

class Car():
    state = True
    def move(self):
        while self.state:
            print('Moving car')
            time.sleep(2)
        print('Stop car')

car1 = Car()

t1 = threading.Thread(target=car1.move)
t1.start()

time.sleep(10)
car1.state = False