
import requests
import csv
import json


def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts[:5]:
            print(post['title'])


def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")
    posts = response.json()
    structured_data = []
    for post in posts:
        entry = {
            'id': post['id'],
            'title': post['title'],
            'body': post['body']
        }
        structured_data.append(entry)
    with open('posts.csv', 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['id', 'title', 'body']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(structured_data)

    print("Done! Data saved to posts.csv")