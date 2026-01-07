#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

# Read Korean HTML
with open('public/lang/ko.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract all FAQ items
pattern = r'<div class="faq-item">.*?<label for="faq\d+" class="faq-question">\s*<i class="fas fa-chevron-down"></i>\s*(.*?)\s*</label>.*?<div class="faq-answer">\s*<p>(.*?)</p>\s*</div>\s*</div>'
matches = re.findall(pattern, html, re.DOTALL)

print(f"총 {len(matches)}개의 FAQ 항목 추출:")
print("=" * 80)
for i, (q, a) in enumerate(matches, 1):
    q = q.strip()
    a = a.strip()
    print(f"{i}. Q: {q}")
    print(f"   A: {a}")
    print("-" * 80)
