import threading

class EvenOdd:
    def __init__(self, max_num):
        self.max_num = max_num
        self.num = 1
        self.lock = threading.Lock()

    def print_even(self):
        while self.num <= self.max_num:
            with self.lock:
                if self.num % 2 == 0:
                    print(f"ChẵnChẵn: {self.num}")
                    self.num += 1

    def print_odd(self):
        while self.num <= self.max_num:
            with self.lock:
                if self.num % 2 != 0:
                    print(f"Lẻ: {self.num}")
                    self.num += 1

if __name__ == "__main__":
    max_num = 20
    eo = EvenOdd(max_num)

    t1 = threading.Thread(target=eo.print_even)
    t2 = threading.Thread(target=eo.print_odd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()