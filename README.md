# Tab Out with Follow-Builders

**Keep tabs on your tabs, and stay updated with AI builders.**

Tab Out with Follow-Builders is an enhanced version of the original Tab Out extension. It not only manages your tab clutter but also brings you daily insights from the world of AI directly to your new tab page.

This project integrates data from [follow-builders](https://github.com/zarazhangrui/follow-builders) and uses **GitHub Actions** to maintain a persistent historical feed.

---

## Enhanced Features

- **Daily AI Feed**: A dedicated bottom section showing the latest insights from AI builders and engineering blogs.
- **Cloud-Side Auto-Sync**: Uses GitHub Actions to automatically fetch and merge new data every 2 hours. Your feed is updated even when your computer is off.
- **Persistent History**: A self-hosted "database" (`data/feed-history.json`) ensures you never miss a post. The extension loads from this central source.
- **Smart Tracking**:
  - **Read/Unread Status**: Red notification badges for new content. Clicking a card marks it as read.
  - **Incremental Loading (Smart Search)**: Defaults to a 3-day view. One click on "加载更早" automatically searches back through history until more content is found, crossing "quiet" days with ease.
  - **Date Separators**: Clean separators for "Today", "Yesterday", and older updates with precise timestamps.
- **Grid Layout**: A clean, responsive card-based layout that distinguishes between 𝕏 posts and technical blogs with color-coded accents.
- **Tab Management**:
  - **See all your tabs at a glance** on a clean grid, grouped by domain.
  - **Homepages group** pulls Gmail inbox, X home, YouTube, LinkedIn, GitHub homepages into one card.
  - **Close tabs with style** with swoosh sound + confetti burst.
  - **Duplicate detection** flags when you have the same page open twice, with one-click cleanup.
  - **Save for later** bookmark tabs to a checklist before closing them.

---

## Manual Setup

**1. Clone the repo**

```bash
git clone https://github.com/neveevol7/tab-out.git
```

**2. Load the Chrome extension**

1. Open Chrome and go to `chrome://extensions`
2. Enable **Developer mode** (top-right toggle)
3. Click **Load unpacked**
4. Navigate to the `extension/` folder inside the cloned repo and select it

**3. Open a new tab**

You'll see Tab Out.

---

## How it works

```
GitHub Action (every 2h) 
  -> Fetches raw data from follow-builders
  -> Merges with data/feed-history.json
  -> Commits back to your repository

You open a new tab
  -> Tab Out fetches history from your GitHub raw URL
  -> Groups tabs by domain
  -> Renders feed with incremental "Smart Search" loading
```

Everything runs inside the Chrome extension and GitHub Actions. Saved tabs are stored in `chrome.storage.local`.

---

## Tech stack

| What | How |
|------|-----|
| Extension | Chrome Manifest V3 |
| Backend | GitHub Actions + Python Sync Script |
| Data | JSON (Self-hosted on GitHub) |
| Storage | chrome.storage.local |
| Sound | Web Audio API (synthesized, no files) |
| Animations | CSS transitions + JS confetti particles |

---

## License

MIT

---

Built by [Zara](https://x.com/zarazhangrui) & [Neal](https://github.com/neveevol7)
