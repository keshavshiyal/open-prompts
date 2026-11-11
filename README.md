<div align="center">

# 🌐 open-prompts

**Treat Prompts as Code. An open-source, modular, and parameterized prompt library for developers, educators, and local AI workflows.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Prompts Count](https://img.shields.io/badge/Prompts-Curated-orange.svg)](#📂-prompt-directory)
[![Live Explorer](https://img.shields.io/badge/Web_UI-GitHub_Pages-purple.svg)](https://keshavshiyal.github.io/open-prompts/)

[🌐 Launch Live Prompt Explorer](https://keshavshiyal.github.io/open-prompts/) • [📐 Prompt Schema](#📐-prompt-architecture) • [⚡ CLI & Ollama Usage](#💻-cli--ollama-integration)

</div>

---

## 💡 Why `open-prompts`?

Most prompt repositories are unorganized text dumps with vague instructions and zero version control. **`open-prompts`** treats prompts like modular software components:

- **🎯 Parameterized Variables:** Strict `{{variable}}` syntax instead of messy `[insert text here]` placeholders.
- **🤖 Model-Aware:** Explicitly tagged with tested models—optimized for both lightweight local models on **Ollama** (3B–8B) and frontier cloud LLMs.
- **📦 Structured Metadata:** Every prompt uses YAML Frontmatter for easy parsing into JSON, CLIs, and web apps.
- **🌐 Zero-Dependency Web UI:** Includes a single-file, offline-ready HTML explorer to fill in variables and copy compiled prompts in one click.

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

Every prompt in `open-prompts` follows a strict Markdown + YAML Frontmatter standard located in [`schemas/prompt-template.md`](./schemas/prompt-template.md):

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
Visit the **[Live Prompt Explorer](https://keshavshiyal.github.io/open-prompts/)** (or open `index.html` locally in any browser):
1. Search or filter prompts by category or tag (`#coding`, `#linux`, `#education`).
2. Enter your custom values into the dynamic variable input fields.
3. Click **Copy Compiled Prompt** and paste it into your LLM of choice.

### 2. Cloning Locally
```bash
git clone [https://github.com/keshavshiyal/open-prompts.git](https://github.com/keshavshiyal/open-prompts.git)
cd open-prompts

# Rebuild the master index.json after adding or editing Markdown prompts
python3 scripts/build-index.py
```

---

## 💻 CLI & Ollama Integration

Pipe prompts from `open-prompts` directly into local models using **Ollama** from your Linux terminal or Termux environment:

```bash
# Example: Inject variables and pipe directly into a local Ollama model
sed -e 's/{{script_goal}}/Backup SQLite files and compress logs daily/g' \
    prompts/linux/bash-script-generator.md | ollama run qwen2.5-coder:7b
```

---

## 🗂️ Repository Structure

```text
open-prompts/
├── prompts/                  # Categorized Markdown prompt files
│   ├── coding/
│   ├── linux/
│   ├── education/
│   ├── data/
│   └── design/
├── schemas/
│   └── prompt-template.md    # Blank template for creating new prompts
├── scripts/
│   └── build-index.py        # Compiles /prompts/*.md into index.json
├── index.json                # Auto-generated JSON database of all prompts
├── index.html                # Zero-dependency single-file Web UI
├── CONTRIBUTING.md           # Guidelines for submitting new prompts
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome! To add a new prompt to `open-prompts`:
1. Copy [`schemas/prompt-template.md`](./schemas/prompt-template.md) into the appropriate `/prompts/<category>/` folder.
2. Ensure all `{{variables}}` used in the prompt body are declared in the YAML frontmatter.
3. Test the prompt on at least one model and include a sample output inside a `<details>` block.
4. Run `python3 scripts/build-index.py` to update `index.json` and submit a Pull Request.

---

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.
