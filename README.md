# Tab Out with Follow-Builders

**Keep tabs on your tabs, and stay updated with AI builders.**

Tab Out with Follow-Builders is an enhanced version of the original Tab Out extension. It not only manages your tab clutter but also brings you daily insights from the world of AI directly to your new tab page.

[中文版 (Chinese Version)](./README_CN.md)

---

## 🚀 Latest Features (New!)

- **One-Click Multi-language Toggle**: Seamlessly switch the entire UI between **English** and **Chinese**. Defaults to your browser's locale while offering manual override.
- **Smart Pre-translation**: All English content from GitHub Trending and Daily Feed is automatically translated and pre-cached via our backend. Enjoy localized content instantly without waiting for API calls.
- **🚀 GitHub Trending Rankings**:
  - **Multi-dimension Switching**: Seamlessly toggle between **Daily** and **Weekly** rankings.
  - **High-Density Insight**: Custom-engineered layout for scanning project descriptions (now translated!), stars, and growth.

## Core Features

- **Daily AI Feed**: A dedicated section showing the latest insights from AI builders and engineering blogs.
  - **Today-First Grouping**: Automatically expands "Today" and collapses history to keep your dashboard focused.
  - **Unread Statistics**: Real-time (unread/total) counts for each date group.
- **Cloud-Side Auto-Sync**: Uses GitHub Actions to automatically fetch and translate new data every 2 hours.
- **Tab Management**:
  - **Grid Layout**: Tabs grouped by domain on a clean grid.
  - **Duplicate detection**: Flags duplicate tabs with one-click cleanup.
  - **Save for later**: Bookmark tabs to a checklist before closing.

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

## Tech stack

| What | How |
|------|-----|
| Extension | Chrome Manifest V3 |
| Backend | GitHub Actions + Python Sync & Translation Script |
| Translation | deep-translator (Google API) |
| Data | JSON (Self-hosted on GitHub) |
| Storage | chrome.storage.local |

---

## License

MIT

---

Built by [Zara](https://x.com/zarazhangrui) & [Neal](https://github.com/neveevol7)
