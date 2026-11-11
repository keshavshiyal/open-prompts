<div align="center">

# 🧩 PromptForge

**Treat Prompts as Code. Modular, parameterized, and battle-tested prompt templates for developers, educators, and local AI workflows.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Prompts Count](https://img.shields.io/badge/Prompts-Curated-orange.svg)](#📂-prompt-directory)
[![Live Explorer](https://img.shields.io/badge/Web_UI-GitHub_Pages-purple.svg)](https://keshavshiyal.github.io/prompt-forge/)

[🌐 Launch Live Prompt Builder](https://keshavshiyal.github.io/prompt-forge/) • [📖 Schema Docs](#📐-prompt-architecture) • [⚡ CLI Usage](#💻-cli--ollama-integration)

</div>

---

## 💡 Why This Repository Exists

Most prompt repositories are unorganized text dumps with vague instructions and zero testing. **PromptForge** treats prompts like modular software components:

- **🎯 Parameterized Variables:** Strict `{{variable}}` syntax instead of messy `[insert text here]` placeholders.
- **🤖 Model-Aware:** Explicitly tagged with recommended parameter sizes (works great with local 3B–8B models on **Ollama** as well as frontier models).
- **📦 Structured Metadata:** Every prompt uses YAML Frontmatter for easy parsing into JSON, CLIs, and web apps.
- **🌐 Zero-Dependency Web UI:** Includes a single-file, offline-ready HTML explorer to fill in variables and copy prompts in one click.

---

## 📂 Prompt Directory

| Category | Description | Path |
| :--- | :--- | :--- |
| 💻 **Coding & Web** | Vanilla JS utilities, PWA scaffolds, IndexedDB schemas, refactoring, and code review. | [`/prompts/coding`](./prompts/coding) |
| 🐧 **Linux & Shell** | Bash automation, log analysis, cron generators, and Termux/server administration. | [`/prompts/linux`](./prompts/linux) |
| 🎓 **Tech Education** | Syllabus breakdowns, lab exercises, bilingual concept explainers, and viva/quiz builders. | [`/prompts/education`](./prompts/education) |
| 📊 **Data & JSON** | Strict JSON/CSV extractors, regex builders, and structured data transformation. | [`/prompts/data`](./prompts/data) |
| 🎨 **Design & UI** | SVG icon generators, CSS layout helpers, and brand asset prompt builders. | [`/prompts/design`](./prompts/design) |

---

## 📐 Prompt Architecture

Every prompt in this repository follows a strict Markdown + YAML Frontmatter standard located in [`schemas/prompt-template.md`](./schemas/prompt-template.md):

```markdown
---
id: "vanilla-pwa-scaffold"
title: "Single-File Offline Utility Generator"
category: "coding"
tags: ["javascript", "html", "pwa", "offline-first"]
models: ["Qwen-2.5-Coder-7B", "Gemini-2.5-Pro"]
temperature: 0.2
variables:
  - name: "app_purpose"
    description: "Core function of the utility application"
    default: "Markdown note-taking app"
  - name: "storage_engine"
    description: "Client-side storage method"
    default: "IndexedDB"
---

## System
You are a senior front-end engineer specializing in zero-dependency, offline-first web applications. Output clean, production-ready code without external CDN libraries.

## Prompt
Create a complete, single-file HTML5 application for a **{{app_purpose}}** using **{{storage_engine}}** for persistent local storage.

### Requirements:
1. Responsive CSS Grid/Flexbox layout with dark mode support.
2. Complete CRUD operations wired to {{storage_engine}}.
3. Export/Import data functionality as JSON.
```

---

## 🚀 Quick Start

### 1. Using the Web Interface (Recommended)
Visit the **[Live Prompt Explorer](https://keshavshiyal.github.io/prompt-forge/)** (or open `index.html` locally in any browser):
1. Search or filter prompts by tag (`#coding`, `#linux`, `#education`).
2. Type your custom values into the dynamic variable input fields.
3. Click **Copy Compiled Prompt** and paste it into your LLM of choice.

### 2. Cloning Locally
```bash
git clone [https://github.com/keshavshiyal/prompt-forge.git](https://github.com/keshavshiyal/prompt-forge.git)
cd prompt-forge

# Rebuild the master index.json after adding new Markdown prompts
python3 scripts/build-index.py
```

---

## 💻 CLI & Ollama Integration

Pipe prompts directly into local models using **Ollama** from your terminal or Termux environment:

```bash
# Example: Run a prompt file directly with Ollama
sed -e 's/{{script_goal}}/Backup PostgreSQL database daily/g' \
    prompts/linux/bash-script-generator.md | ollama run qwen2.5-coder:7b
```

---

## 🗂️ Repository Structure

```text
prompt-forge/
├── prompts/                  # Categorized Markdown prompt files
│   ├── coding/
│   ├── linux/
│   ├── education/
│   ├── data/
│   └── design/
├── schemas/
│   └── prompt-template.md    # Blank template for new prompts
├── scripts/
│   └── build-index.py        # Compiles /prompts/*.md into index.json
├── index.json                # Auto-generated JSON database of all prompts
├── index.html                # Zero-dependency single-file Web UI
├── CONTRIBUTING.md           # Guidelines for submitting new prompts
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome! To add a new prompt:
1. Copy [`schemas/prompt-template.md`](./schemas/prompt-template.md) into the appropriate `/prompts/<category>/` folder.
2. Ensure all `{{variables}}` in the prompt body are declared in the YAML frontmatter.
3. Test the prompt on at least one model and include a sample output inside a `<details>` block.
4. Run `python3 scripts/build-index.py` and submit a Pull Request.

---

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.
