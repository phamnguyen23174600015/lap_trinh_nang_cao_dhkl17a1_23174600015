import threading

def print_even_numbers():
    for i in range(30, 51):
        if i % 2 == 0:
            print(f"ChẵnChẵn: {i}")

def print_odd_numbers():
    for i in range(30, 51):
        if i % 2 != 0:
            print(f"Lẻ: {i}")

if __name__ == "__main__":
    even_thread = threading.Thread(target=print_even_numbers)
    odd_thread = threading.Thread(target=print_odd_numbers)

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()