import os
import json
import requests
from datetime import datetime

BLOGS_URL = 'https://raw.githubusercontent.com/zarazhangrui/follow-builders/main/feed-blogs.json'
X_URL = 'https://raw.githubusercontent.com/zarazhangrui/follow-builders/main/feed-x.json'
HISTORY_FILE = 'data/feed-history.json'

def sync():
    os.makedirs('data', exist_ok=True)
    history = []
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                history = json.load(f)
        except Exception as e:
            print(f"Error reading history: {e}")
            history = []
    
    item_map = {item['url']: item for item in history}

    try:
        blogs_res = requests.get(BLOGS_URL).json()
        x_res = requests.get(X_URL).json()

        for b in blogs_res.get('blogs', []):
            item_map[b['url']] = {
                'url': b['url'],
                'type': 'blog',
                'name': b['name'],
                'title': b['title'],
                'date': b.get('publishedAt') or blogs_res.get('generatedAt')
            }

        for builder in x_res.get('x', []):
            for tweet in builder.get('tweets', []):
                item_map[tweet['url']] = {
                    'url': tweet['url'],
                    'type': 'x',
                    'name': builder['name'],
                    'title': tweet['text'],
                    'date': tweet['createdAt']
                }

        new_history = sorted(item_map.values(), key=lambda x: x['date'], reverse=True)
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(new_history, f, ensure_ascii=False, indent=2)
        print(f"Sync complete. Total items: {len(new_history)}")

    except Exception as e:
        print(f"Sync failed: {e}")

if __name__ == '__main__':
    sync()
