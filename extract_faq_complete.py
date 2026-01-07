#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import json

# Read Korean HTML
with open('public/lang/ko.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract FAQ items with improved pattern
faq_items = []
pattern = r'<div class="faq-item">.*?<input type="checkbox" id="(faq\d+)".*?<label for="\1" class="faq-question">.*?<span>(.*?)</span>.*?</label>.*?<div class="faq-answer">\s*(.*?)\s*</div>'

matches = re.findall(pattern, html, re.DOTALL)

for faq_id, question, answer in matches:
    question = question.strip()
    answer = answer.strip()
    faq_items.append({
        'id': faq_id,
        'question': question,
        'answer': answer
    })

print(f"총 {len(faq_items)}개의 FAQ 항목 추출 완료")
print("=" * 100)

for item in faq_items:
    print(f"{item['id']}: {item['question']}")
    print(f"   답변: {item['answer']}")
    print("-" * 100)

# Save to JSON
with open('faq_korean.json', 'w', encoding='utf-8') as f:
    json.dump(faq_items, f, ensure_ascii=False, indent=2)

print(f"\n✅ FAQ 데이터를 faq_korean.json에 저장했습니다.")
