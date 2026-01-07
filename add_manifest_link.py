#!/usr/bin/env python3
"""
모든 HTML에 manifest.json 절대경로 추가
"""
import re
import os

languages = ['ko', 'en', 'zh-CN', 'zh-TW', 'ja', 'hi', 'es', 'fr', 'ar', 'bn', 'ru', 'pt']

for lang in languages:
    file_path = f'/home/user/webapp/public/lang/{lang}.html'
    
    if not os.path.exists(file_path):
        print(f"⚠️  {lang}.html 파일이 없습니다.")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # manifest.json이 이미 있으면 스킵
    if 'manifest.json' in html:
        print(f"⏭️  {lang}.html - manifest 이미 존재")
        continue
    
    # <link href="https://cdn.jsdelivr.net/npm/@fortawesome... 바로 다음에 추가
    html = html.replace(
        '<link href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css" rel="stylesheet">',
        '<link href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css" rel="stylesheet">\n    <link rel="manifest" href="/manifest.json">'
    )
    
    print(f"✅ {lang}.html 수정 완료")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

print("\n✅ 모든 HTML 파일에 manifest.json 추가 완료!")
print("   - 절대경로: /manifest.json")
