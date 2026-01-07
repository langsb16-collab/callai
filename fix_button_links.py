#!/usr/bin/env python3
"""
버튼 링크를 /demo.html과 /signup.html로 수정
"""
import re
import os

languages = ['ko', 'en', 'zh-CN', 'zh-TW', 'ja', 'hi', 'es', 'fr', 'ar', 'bn', 'ru', 'pt']

# 버튼 텍스트 매핑
btn_mapping = {
    'ko': {'signup': '무료로 시작하기', 'demo': '데모 보기'},
    'en': {'signup': 'Start Free', 'demo': 'Watch Demo'},
    'zh-CN': {'signup': '免费开始', 'demo': '观看演示'},
    'zh-TW': {'signup': '免費開始', 'demo': '觀看演示'},
    'ja': {'signup': '無料で始める', 'demo': 'デモを見る'},
    'hi': {'signup': 'मुफ़्त शुरू करें', 'demo': 'डेमो देखें'},
    'es': {'signup': 'Comenzar Gratis', 'demo': 'Ver Demo'},
    'fr': {'signup': 'Commencer Gratuitement', 'demo': 'Voir la Démo'},
    'ar': {'signup': 'ابدأ مجانًا', 'demo': 'مشاهدة العرض'},
    'bn': {'signup': 'বিনামূল্যে শুরু করুন', 'demo': 'ডেমো দেখুন'},
    'ru': {'signup': 'Начать бесплатно', 'demo': 'Посмотреть демо'},
    'pt': {'signup': 'Começar Grátis', 'demo': 'Ver Demo'}
}

for lang in languages:
    file_path = f'/home/user/webapp/public/lang/{lang}.html'
    
    if not os.path.exists(file_path):
        print(f"⚠️  {lang}.html 파일이 없습니다.")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # /signup 링크 변경
    html = re.sub(
        r'href="/signup"',
        'href="/signup.html"',
        html
    )
    
    # /demo 링크 변경
    html = re.sub(
        r'href="/demo"',
        'href="/demo.html"',
        html
    )
    
    print(f"✅ {lang}.html 수정 완료")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

print("\n✅ 모든 HTML 파일 버튼 링크 수정 완료!")
print("   - /signup → /signup.html")
print("   - /demo → /demo.html")
