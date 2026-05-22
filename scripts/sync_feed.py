import os
import json
import requests
import re
from datetime import datetime
from deep_translator import GoogleTranslator

BLOGS_URL = 'https://raw.githubusercontent.com/zarazhangrui/follow-builders/main/feed-blogs.json'
X_URL = 'https://raw.githubusercontent.com/zarazhangrui/follow-builders/main/feed-x.json'
HISTORY_FILE = 'data/feed-history.json'
TRENDING_FILE = 'data/github-trending.json'

def translate_text(text):
    try:
        if not text or text.strip() == "":
            return ""
        # Using GoogleTranslator for better quality and stability
        translated = GoogleTranslator(source='auto', target='zh-CN').translate(text)
        return translated
    except Exception as e:
        print(f"Translation failed for '{text[:20]}...': {e}")
        return text

def parse_github_readme(markdown):
    # 1. Extract the Ranking Table
    table_regex = r'\|\s*(\d+)\s*\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*([^|]+)\|\s*([^|]+)\|'
    projects = []
    for match in re.finditer(table_regex, markdown):
        projects.append({
            'rank': match.group(1),
            'name': match.group(2),
            'url': match.group(3),
            'stars': match.group(4).strip(),
            'growth': match.group(5).strip()
        })

    # 2. Extract Descriptions
    desc_map = {}
    detail_sections = markdown.split('<h3')
    for sec in detail_sections:
        url_match = re.search(r'https://github\.com/([a-zA-Z0-9-._]+/[a-zA-Z0-9-._]+)', sec)
        desc_match = re.search(r'📝\s*项目描述[:：]\s*([^\n<]+)', sec)
        if url_match and desc_match:
            desc_map[url_match.group(1)] = desc_match.group(1).strip()
    
    for p in projects:
        p['description'] = desc_map.get(p['name'], "No description available.")
        if p['description'] != "No description available.":
            print(f"Translating GitHub desc: {p['name']}...")
            p['description_cn'] = translate_text(p['description'])
        else:
            p['description_cn'] = ""
            
    return projects

def sync_github_trending():
    print("Syncing GitHub Trending...")
    daily_url = 'https://raw.githubusercontent.com/OpenGithubs/github-daily-rank/main/README.md'
    weekly_url = 'https://raw.githubusercontent.com/OpenGithubs/github-weekly-rank/main/README.md'
    
    try:
        daily_md = requests.get(daily_url).text
        weekly_md = requests.get(weekly_url).text
        
        data = {
            'daily': parse_github_readme(daily_md),
            'weekly': parse_github_readme(weekly_md),
            'updated_at': datetime.now().isoformat()
        }
        
        with open(TRENDING_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("GitHub Trending sync complete.")
    except Exception as e:
        print(f"GitHub Trending sync failed: {e}")

def sync_feed():
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

        # Process Blogs
        for b in blogs_res.get('blogs', []):
            url = b['url']
            if url not in item_map or 'title_cn' not in item_map[url]:
                print(f"Translating blog: {b['title'][:30]}...")
                item_map[url] = {
                    'url': url,
                    'type': 'blog',
                    'name': b['name'],
                    'title': b['title'],
                    'title_cn': translate_text(b['title']),
                    'date': b.get('publishedAt') or blogs_res.get('generatedAt')
                }

        # Process X (Tweets)
        for builder in x_res.get('x', []):
            for tweet in builder.get('tweets', []):
                url = tweet['url']
                if url not in item_map or 'title_cn' not in item_map[url]:
                    print(f"Translating tweet from {builder['name']}...")
                    item_map[url] = {
                        'url': url,
                        'type': 'x',
                        'name': builder['name'],
                        'title': tweet['text'],
                        'title_cn': translate_text(tweet['text']),
                        'date': tweet['createdAt']
                    }

        # Final pass: Ensure EVERYTHING has a translation (for legacy items)
        for url, item in item_map.items():
            if 'title_cn' not in item:
                print(f"Retroactive translation: {item['title'][:30]}...")
                item['title_cn'] = translate_text(item['title'])

        new_history = sorted(item_map.values(), key=lambda x: x['date'], reverse=True)
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(new_history, f, ensure_ascii=False, indent=2)
        print(f"Feed sync complete. Total items: {len(new_history)}")

    except Exception as e:
        print(f"Feed sync failed: {e}")

if __name__ == '__main__':
    sync_feed()
    sync_github_trending()
