---
id: "vanilla-pwa-scaffold"
title: "Single-File Offline Utility Generator"
category: "coding"
tags: ["vanilla-js", "html5", "pwa", "indexeddb", "offline-first"]
models: ["Qwen-2.5-Coder-7B", "Gemini-2.5-Pro"]
temperature: 0.2
variables:
  - name: "app_purpose"
    description: "Core utility goal of the web app"
    default: "Trainee Attendance & Record Tracker"
  - name: "storage_engine"
    description: "Client-side persistence engine"
    default: "IndexedDB"
---

## System
You are an expert front-end architect specializing in zero-dependency, offline-first single-file web applications. Output clean, complete, production-ready code without external JS or CSS CDN links.

## Prompt
Build a complete, self-contained single-file HTML application (`index.html`) for a **{{app_purpose}}** using **{{storage_engine}}**.

### Technical Requirements:
1. **Zero Dependencies:** Pure Vanilla HTML5, CSS3, and ES6+ JavaScript in one file.
2. **Persistence:** Full CRUD operations wired to **{{storage_engine}}**.
3. **Data Portability:** Include one-click JSON export and import buttons.
4. **UI/UX:** Responsive dark/light theme layout with live search filtering and keyboard shortcuts.