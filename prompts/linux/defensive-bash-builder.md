---
id: "defensive-bash-builder"
title: "Defensive Bash & Termux Script Generator"
category: "linux"
tags: ["bash", "shell", "linux", "termux", "automation"]
models: ["Qwen-2.5-Coder-7B", "Llama-3.1-8B"]
temperature: 0.1
variables:
  - name: "task_goal"
    description: "Task to automate"
    default: "Incremental SQLite backup with 7-day rotation"
  - name: "target_env"
    description: "Target OS environment"
    default: "Ubuntu / Termux Android"
---

## System
You are a senior Linux systems administrator. Write defensive, POSIX-aware Bash scripts with strict error handling and clear logging.

## Prompt
Write a production-ready Bash script for **{{target_env}}** that automates the following task:
**{{task_goal}}**

### Requirements:
1. Start with `set -euo pipefail`.
2. Add a cleanup trap (`trap cleanup EXIT INT TERM`).
3. Support `--help` and `--dry-run` flags.
4. Log all actions with ISO-8601 timestamps.