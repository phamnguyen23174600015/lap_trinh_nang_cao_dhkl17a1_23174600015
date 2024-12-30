import threading
import time
from datetime import datetime

# Hàm cho luồng Google
def google_thread():
    print("Starting Google")
    for _ in range(5):  # Google in thông báo 5 lần
        time.sleep(1)  # Tạm dừng 1 giây
        print(f"Google: Web {datetime.now().strftime('%b %d %H:%M:%S %Y')}")
    print("Exiting Google")

# Hàm cho luồng Yahoo
def yahoo_thread():
    print("Starting Yahoo")
    for _ in range(4):  # Yahoo in thông báo 4 lần
        time.sleep(2)  # Tạm dừng 2 giây
        print(f"Yahoo: Web {datetime.now().strftime('%b %d %H:%M:%S %Y')}")
    print("Exiting Yahoo")

# Hàm cho luồng Facebook
def facebook_thread():
    print("Starting Facebook")
    for _ in range(5):  # Facebook in thông báo 5 lần
        time.sleep(3)  # Tạm dừng 3 giây
        print(f"Facebook: Web {datetime.now().strftime('%b %d %H:%M:%S %Y')}")
    print("Exiting Facebook")

# Hàm chính
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
    
    # Chờ các luồng hoàn thành
    google.join()
    yahoo.join()
    facebook.join()
    
    print("Exiting Main Thread")

if __name__ == "__main__":
    main()
