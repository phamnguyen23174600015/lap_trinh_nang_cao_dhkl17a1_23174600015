import threading
import time
from datetime import datetime

# Hàm cho từng luồng
def google_thread():
    print("Starting Google")
    for i in range(3):
        time.sleep(1)  # Tạm dừng 1 giây
        print(f"Google: Web {datetime.now().strftime('%b %d %H:%M:%S %Y')}")
    print("Exiting Google")

def yahoo_thread():
    print("Starting Yahoo")
    for i in range(4):
        time.sleep(2)  # Tạm dừng 2 giây
        print(f"Yahoo: Web {datetime.now().strftime('%b %d %H:%M:%S %Y')}")
    print("Exiting Yahoo")

def facebook_thread():
    print("Starting Facebook")
    for i in range(5):
        time.sleep(3)  # Tạm dừng 3 giây
        print(f"Facebook: Web {datetime.now().strftime('%b %d %H:%M:%S %Y')}")
    print("Exiting Facebook")

def main():
    print("Starting Main Thread")
    
    # Tạo các luồng
    google = threading.Thread(target=google_thread)
    yahoo = threading.Thread(target=yahoo_thread)
    facebook = threading.Thread(target=facebook_thread)
    
    # Bắt đầu các luồng
    google.start()
    yahoo.start()
    facebook.start()
    
    # Chờ các luồng kết thúc
    google.join()
    yahoo.join()
    facebook.join()
    
    print("Exiting Main Thread")

if __name__ == "__main__":
    main()
