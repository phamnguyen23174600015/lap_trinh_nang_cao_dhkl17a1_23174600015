import threading

def print_thread_name():
    print(f'Tên luồng: {threading.current_thread().name}')

threads = []
for i in range(5):
    thread = threading.Thread(target=print_thread_name, name=f'Luồng-{i+1}')
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()