/**
 * background.js — Service Worker for Badge Updates & Background Fetch
 *
 * Chrome's "always-on" background script for Tab Out.
 * Tasks:
 * 1. Keep the toolbar badge showing the current open tab count.
 * 2. Periodically fetch builders feed in the background.
 */

// ─── Badge updater ────────────────────────────────────────────────────────────

async function updateBadge() {
  try {
    const tabs = await chrome.tabs.query({});
    const count = tabs.filter(t => {
      const url = t.url || '';
      return (
        !url.startsWith('chrome://') &&
        !url.startsWith('chrome-extension://') &&
        !url.startsWith('about:') &&
        !url.startsWith('edge://') &&
        !url.startsWith('brave://')
      );
    }).length;

    await chrome.action.setBadgeText({ text: count > 0 ? String(count) : '' });

    if (count === 0) return;

    let color;
    if (count <= 10) {
      color = '#3d7a4a'; 
    } else if (count <= 20) {
      color = '#b8892e'; 
    } else {
      color = '#b35a5a'; 
    }

    await chrome.action.setBadgeBackgroundColor({ color });

  } catch {
    chrome.action.setBadgeText({ text: '' });
  }
}

// ─── Background Fetch ─────────────────────────────────────────────────────────

const BLOGS_URL = 'https://raw.githubusercontent.com/zarazhangrui/follow-builders/main/feed-blogs.json';
const X_URL     = 'https://raw.githubusercontent.com/zarazhangrui/follow-builders/main/feed-x.json';

/**
 * fetchAndCacheFeed()
 *
 * Fetches the latest data from GitHub and merges it into the local cache.
 */
async function fetchAndCacheFeed() {
  console.log('[tab-out] Background fetching builders feed...');
  try {
    const [blogsRes, xRes] = await Promise.all([
      fetch(BLOGS_URL).then(r => r.json()),
      fetch(X_URL).then(r => r.json())
    ]);

    const blogs = blogsRes.blogs || [];
    const builders = xRes.x || [];

    const freshItems = [
      ...blogs.map(b => ({ 
        url: b.url, 
        type: 'blog', 
        name: b.name, 
        title: b.title, 
        date: b.publishedAt || blogsRes.generatedAt 
      })),
    ];

    builders.forEach(builder => {
      (builder.tweets || []).forEach(tweet => {
        freshItems.push({
          url: tweet.url,
          type: 'x',
          name: builder.name,
          title: tweet.text,
          date: tweet.createdAt
        });
      });
    });

    const { cachedFeedItems = [] } = await chrome.storage.local.get('cachedFeedItems');
    const itemMap = new Map();
    
    cachedFeedItems.forEach(item => itemMap.set(item.url, item));
    freshItems.forEach(item => itemMap.set(item.url, item));

    const combined = Array.from(itemMap.values())
      .sort((a, b) => new Date(b.date) - new Date(a.date));

    await chrome.storage.local.set({ cachedFeedItems: combined });
    console.log(`[tab-out] Background fetch complete. Cache size: ${combined.length}`);

  } catch (err) {
    console.warn('[tab-out] Background fetch failed:', err);
  }
}

// ─── Event listeners ──────────────────────────────────────────────────────────

chrome.runtime.onInstalled.addListener(() => {
  updateBadge();
  chrome.alarms.create('fetchFeedAlarm', { periodInMinutes: 30 });
  fetchAndCacheFeed();
});

chrome.runtime.onStartup.addListener(() => {
  updateBadge();
  fetchAndCacheFeed();
});

chrome.alarms.onAlarm.addListener((alarm) => {
  if (alarm.name === 'fetchFeedAlarm') {
    fetchAndCacheFeed();
  }
});

chrome.tabs.onCreated.addListener(() => updateBadge());
chrome.tabs.onRemoved.addListener(() => updateBadge());
chrome.tabs.onUpdated.addListener(() => updateBadge());

// Initial run
updateBadge();
