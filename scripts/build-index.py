#!/usr/bin/env python3
"""
Compiles all Markdown prompt files in /prompts/**/*.md into index.json.
Preserves full variable metadata (name, description, default) using zero external dependencies.
"""
import json
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT_DIR / "prompts"
OUTPUT_FILE = ROOT_DIR / "index.json"

def parse_frontmatter(fm_text: str, filepath: Path) -> dict:
    meta = {
        "id": filepath.stem,
        "title": filepath.stem.replace("-", " ").title(),
        "category": filepath.parent.name,
        "tags": [],
        "models": [],
        "temperature": 0.2,
        "variables": []
    }

    lines = fm_text.splitlines()
    in_variables = False
    current_var = None

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if stripped.startswith("variables:"):
            in_variables = True
            continue

        if in_variables:
            if stripped.startswith("- name:"):
                if current_var:
                    meta["variables"].append(current_var)
                val = stripped.split(":", 1)[1].strip().strip('"\'')
                current_var = {"name": val, "description": "", "default": ""}
            elif current_var and stripped.startswith("description:"):
                current_var["description"] = stripped.split(":", 1)[1].strip().strip('"\'')
            elif current_var and stripped.startswith("default:"):
                current_var["default"] = stripped.split(":", 1)[1].strip().strip('"\'')
            elif not line.startswith(" ") and not line.startswith("\t"):
                in_variables = False
                if current_var:
                    meta["variables"].append(current_var)
                    current_var = None

        if not in_variables and ":" in stripped:
            key, val = [x.strip() for x in stripped.split(":", 1)]
            if key in ["id", "title", "category"] and val:
                meta[key] = val.strip('"\'')
            elif key == "temperature" and val:
                try:
                    meta[key] = float(val)
                except ValueError:
                    pass
            elif key in ["tags", "models"] and val.startswith("["):
                try:
                    meta[key] = json.loads(val)
                except Exception:
                    pass

    if current_var:
        meta["variables"].append(current_var)

    return meta

def parse_markdown_prompt(filepath: Path):
    text = filepath.read_text(encoding="utf-8")
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.DOTALL)
    if not fm_match:
        return None

    fm_text, body = fm_match.groups()
    meta = parse_frontmatter(fm_text, filepath)

    sys_match = re.search(r"##\s*System\s*\n(.*?)(?=\n##\s*Prompt|\Z)", body, re.DOTALL | re.IGNORECASE)
    prm_match = re.search(r"##\s*Prompt\s*\n(.*?)(?=\n##\s*|\Z)", body, re.DOTALL | re.IGNORECASE)

    meta["system"] = sys_match.group(1).strip() if sys_match else ""
    meta["prompt"] = prm_match.group(1).strip() if prm_match else body.strip()

    # Auto-detect any {{variables}} in body not declared in frontmatter
    declared = {v["name"] for v in meta["variables"]}
    for v_name in dict.fromkeys(re.findall(r"\{\{\s*([a-zA-Z0-9_]+)\s*\}\}", meta["prompt"])):
        if v_name not in declared:
            meta["variables"].append({"name": v_name, "description": f"Value for {v_name}", "default": ""})

    return meta

def main():
    prompts = []
    for md_file in sorted(PROMPTS_DIR.rglob("*.md")):
        parsed = parse_markdown_prompt(md_file)
        if parsed:
            prompts.append(parsed)

    OUTPUT_FILE.write_text(json.dumps(prompts, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SUCCESS] Compiled {len(prompts)} prompts into {OUTPUT_FILE}")

if __name__ == "__main__":
    main()