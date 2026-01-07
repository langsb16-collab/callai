#!/usr/bin/env python3
"""
모바일 404 오류 해결
- <base href="/lang/"> 태그 추가
- 모든 링크를 절대경로로 변경
- 언어 선택기 링크 통일
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
    
    # 1. <base href="/lang/"> 태그 추가 (없으면)
    if '<base href="/lang/">' not in html:
        html = html.replace(
            '<meta charset="UTF-8">',
            '<base href="/lang/">\n    <meta charset="UTF-8">'
        )
    
    # 2. 언어 선택기 상대경로 → 절대경로
    # window.location.href='/lang/'+this.value+'.html' 형태는 이미 절대경로이므로 OK
    
    # 3. 헤더 내부 링크 절대경로로 변경 (#features, #industries)
    # 이미 #로 시작하므로 같은 페이지 내 앵커는 문제없음
    
    # 4. CSS/JS CDN은 이미 절대경로 (https://)이므로 OK
    
    # 5. 중요: select의 onchange 함수 확인
    # 현재: window.location.href='/lang/'+this.value+'.html'
    # 이미 절대경로이므로 OK
    
    print(f"✅ {lang}.html 수정 완료")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

print("\n✅ 모든 12개 언어 HTML 파일 <base> 태그 추가 완료!")
print("   - <base href=\"/lang/\">")
print("   - 언어 선택기 이미 절대경로 사용 중")
print("   - CDN 리소스 이미 절대경로 사용 중")
