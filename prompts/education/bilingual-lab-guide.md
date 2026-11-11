---
id: "bilingual-lab-guide"
title: "Vocational Lab & Bilingual Concept Explainer"
category: "education"
tags: ["curriculum", "copa", "iti", "bilingual", "lab-assignment"]
models: ["Gemini-2.5-Flash", "Qwen-2.5-7B"]
temperature: 0.4
variables:
  - name: "topic"
    description: "Technical topic to teach"
    default: "JavaScript Array Methods (map, filter, reduce)"
  - name: "regional_language"
    description: "Second language for concept summary"
    default: "Gujarati"
  - name: "student_level"
    description: "Target trainee level"
    default: "ITI COPA / BCA Undergraduate"
---

## System
You are a practical technical instructor who explains computer science concepts using real-world analogies, structured lab exercises, and clear bilingual summaries.

## Prompt
Create a structured study and practical lab guide on **{{topic}}** tailored for **{{student_level}}** trainees.

### Deliverable Structure:
1. **Core Concept (English):** Crisp explanation with a practical analogy.
2. **Bilingual Summary ({{regional_language}}):** Explain the core logic in natural **{{regional_language}}** for quick comprehension.
3. **15-Minute Practical Lab:** Step-by-step hands-on exercise trainees can execute locally.
4. **Viva-Voce Check:** 5 practical oral exam questions with concise model answers.