import requests

api = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(api)

if response.status_code == 200:
    posts = response.json()

    print(f"tổng sô bài post: {len(posts)}")

    for post in posts:
        print(f"UserID: {post['userId']}, ID: {post['id']}, Title: {post['title']}")
        print(f"Body: {post['body']}\n")
else:
    print(f"Lỗi . Mã trạng thái: {response.status_code}")
