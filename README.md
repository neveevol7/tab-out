# Tab Out with Follow-Builders

**Keep tabs on your tabs, and stay updated with AI builders.**

Tab Out with Follow-Builders is an enhanced version of the original Tab Out extension. It not only manages your tab clutter but also brings you daily insights from the world of AI directly to your new tab page.

This project integrates data from [follow-builders](https://github.com/zarazhangrui/follow-builders) to show you what AI engineers and product builders are talking about on X and their blogs.

---

## Enhanced Features

- **Daily AI Feed**: A dedicated bottom section showing the latest insights from AI builders and engineering blogs.
- **Smart Tracking**:
  - **Read/Unread Status**: Red notification badges for new content. Clicking a card marks it as read, turning the badge grey and fading the card for better focus.
  - **3-Day History & Caching**: The extension automatically caches updates locally. Even if the source clears its daily feed, you'll see a rolling 3-day history grouped by date.
  - **Date Separators**: Clean separators for "Today", "Yesterday", and older updates with precise timestamps.
- **Grid Layout**: A clean, responsive card-based layout that distinguishes between 𝕏 posts and technical blogs with color-coded accents.
- **Tab Management**:
  - **See all your tabs at a glance** on a clean grid, grouped by domain.
  - **Homepages group** pulls Gmail inbox, X home, YouTube, LinkedIn, GitHub homepages into one card.
  - **Close tabs with style** with swoosh sound + confetti burst.
  - **Duplicate detection** flags when you have the same page open twice, with one-click cleanup.
  - **Save for later** bookmark tabs to a checklist before closing them.
- **100% Privacy**: Your tab data never leaves your machine. The feed is fetched directly from GitHub with no intermediate servers.

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
You open a new tab
  -> Tab Out shows your open tabs grouped by domain
  -> Homepages (Gmail, X, etc.) get their own group at the top
  -> Click any tab title to jump to it
  -> Close groups you're done with (swoosh + confetti)
  -> Save tabs for later before closing them
```

Everything runs inside the Chrome extension. No external server, no API calls, no data sent anywhere. Saved tabs are stored in `chrome.storage.local`.

---

## Tech stack

| What | How |
|------|-----|
| Extension | Chrome Manifest V3 |
| Storage | chrome.storage.local |
| Sound | Web Audio API (synthesized, no files) |
| Animations | CSS transitions + JS confetti particles |

---

## License

MIT

---

Built by [Zara](https://x.com/zarazhangrui)
