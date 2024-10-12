import requests

api = "https://jsonplaceholder.typicode.com/comments?postId=1"

response = requests.get(api)

if response.status_code == 200:
    posts = response.json()

    print("danh sách các bình luận postId = 1:")

    for post in posts:
        print(f"postID: {post['id']}, Name: {post['name']}, Email: {post['email']}")
        print(f"Body: {post['body']}\n")

    print("danh sách các bình luận gới hạn 3:")
    for post in posts[:3]:
        print(f"postID: {post['id']}, Name: {post['name']}, Email: {post['email']}")
        print(f"Body: {post['body']}\n")

else:
    print(f"Lỗi . Mã trạng thái: {response.status_code}")
