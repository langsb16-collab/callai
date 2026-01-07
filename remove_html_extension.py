#!/usr/bin/env python3
"""
언어 선택기 URL에서 .html 확장자 제거
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
    
    # 언어 선택기 URL 수정: .html 제거
    html = html.replace(
        "window.location.href='/lang/'+this.value+'.html'",
        "window.location.href='/lang/'+this.value"
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ {lang}.html - 언어 선택기 URL 수정 완료")

print("\n✅ 모든 파일 수정 완료! URL: /lang/ko (확장자 없음)")
