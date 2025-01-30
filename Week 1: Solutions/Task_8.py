import requests
import json

from dataclasses import dataclass

@dataclass
class Post:
    userId: int
    id: int
    title: str
    body: str


posts = []

for i in range(1,4):
    URL = f"https://jsonplaceholder.typicode.com/posts/{i}"

    response = requests.get(URL)
    post_data = json.loads(response.content)

    post = Post(userId=post_data["userId"], id=post_data['id'], title=post_data['title'], body=post_data['body'])
    posts.append(post)

posts.reverse()
for post in posts:
    print(f"Post {4-post.id}")
    print(f"\t User ID: {post.userId}")
    print(f"\t ID: {post.id}")
    print(f"\t Title: {post.title}")
    print(f"\t Body: {post.body}")