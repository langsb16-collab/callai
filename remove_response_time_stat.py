#!/usr/bin/env python3
"""
통계 섹션에서 '< 1초'와 '응답 속도' 텍스트 삭제
11개 언어 (한국어 제외: en, zh-CN, zh-TW, ja, hi, es, fr, ar, bn, ru, pt)
"""
import re
import os

# 한국어 제외 11개 언어
languages = ['en', 'zh-CN', 'zh-TW', 'ja', 'hi', 'es', 'fr', 'ar', 'bn', 'ru', 'pt']

for lang in languages:
    file_path = f'/home/user/webapp/public/lang/{lang}.html'
    
    if not os.path.exists(file_path):
        print(f"⚠️  {lang}.html 파일이 없습니다.")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 통계 섹션에서 4번째 stat (< 1초 / 응답 속도) 전체 삭제
    # <div><div class="text-3xl font-bold">< 1초</div><div class="text-sm">응답 속도</div></div> 형태
    
    # 패턴 1: < 1초 관련
    html = re.sub(
        r'<div><div class="text-3xl font-bold">&lt;\s*1[^<]*</div><div class="text-sm">[^<]*</div></div>',
        '',
        html,
        flags=re.IGNORECASE
    )
    
    # 패턴 2: Response Time / 応答速度 등 다양한 번역
    html = re.sub(
        r'<div><div class="text-3xl font-bold">[^<]*[1-9][^<]*</div><div class="text-sm">[Rr]esponse.*?</div></div>',
        '',
        html,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    # grid-cols-4를 grid-cols-3으로 변경
    html = html.replace('grid-cols-4', 'grid-cols-3')
    html = html.replace('md:grid-cols-4', 'md:grid-cols-3')
    
    print(f"✅ {lang}.html 수정 완료")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

print("\n✅ 11개 언어 통계 섹션 수정 완료!")
print("   - '< 1초' 텍스트 삭제")
print("   - '응답 속도' 텍스트 삭제")
print("   - 그리드 레이아웃: 4열 → 3열")
