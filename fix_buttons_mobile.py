#!/usr/bin/env python3
"""
모든 언어 HTML 파일에 버튼 URL 수정 및 모바일 최적화 적용
"""
import re
import os

# 12개 언어 코드
languages = ['ko', 'en', 'zh-CN', 'zh-TW', 'ja', 'hi', 'es', 'fr', 'ar', 'bn', 'ru', 'pt']

# 버튼 텍스트 번역 (translations_all_11.json에서 가져온 값)
btn_texts = {
    'ko': {'start': '무료로 시작하기', 'demo': '데모 보기'},
    'en': {'start': 'Start Free', 'demo': 'Watch Demo'},
    'zh-CN': {'start': '免费开始', 'demo': '观看演示'},
    'zh-TW': {'start': '免費開始', 'demo': '觀看演示'},
    'ja': {'start': '無料で始める', 'demo': 'デモを見る'},
    'hi': {'start': 'मुफ़्त शुरू करें', 'demo': 'डेमो देखें'},
    'es': {'start': 'Comenzar Gratis', 'demo': 'Ver Demo'},
    'fr': {'start': 'Commencer Gratuitement', 'demo': 'Voir la Démo'},
    'ar': {'start': 'ابدأ مجانًا', 'demo': 'مشاهدة العرض'},
    'bn': {'start': 'বিনামূল্যে শুরু করুন', 'demo': 'ডেমো দেখুন'},
    'ru': {'start': 'Начать бесплатно', 'demo': 'Посмотреть демо'},
    'pt': {'start': 'Começar Grátis', 'demo': 'Ver Demo'}
}

for lang in languages:
    file_path = f'/home/user/webapp/public/lang/{lang}.html'
    
    if not os.path.exists(file_path):
        print(f"⚠️  {lang}.html 파일이 없습니다. 건너뜁니다.")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. CSS 스타일 추가 (없으면)
    if '@media (max-width: 640px)' not in html:
        css_style = '''    <style>
        @media (max-width: 640px) {
            .mobile-compact { font-size: 0.875rem; }
            .mobile-title { font-size: 1rem !important; }
            .mobile-btn { font-size: 0.75rem; padding: 0.5rem 1rem; }
        }
    </style>'''
        html = html.replace('</head>', f'{css_style}\n</head>')
    
    # 2. 로고 글자 크기 축소 (모바일)
    html = re.sub(
        r'<i class="fas fa-phone-volume text-purple-600 text-xl"></i>',
        '<i class="fas fa-phone-volume text-purple-600 text-base sm:text-xl"></i>',
        html
    )
    html = re.sub(
        r'<span class="font-bold text-xl">CallMind AI</span>',
        '<span class="font-bold text-base sm:text-xl mobile-title">CallMind AI</span>',
        html
    )
    
    # 3. 헤더 네비게이션 반응형 수정
    # 기존 nav를 hidden md:flex로 변경
    html = re.sub(
        r'<nav class="flex items-center space-x-6">',
        '<nav class="hidden md:flex items-center space-x-6">',
        html
    )
    
    # select 박스 크기 축소
    html = re.sub(
        r'<select onchange="window\.location\.href=\'/lang/\'\+this\.value\+\'\.html\'" class="border rounded px-2 py-1">',
        '<select onchange="window.location.href=\'/lang/\'+this.value+\'.html\'" class="border rounded px-2 py-1 text-sm">',
        html
    )
    
    # 헤더 "무료로 시작하기" 버튼 URL 수정 (각 언어별)
    html = re.sub(
        r'<a href="#features" class="bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700">([^<]+)</a>\s*</nav>',
        f'<a href="/signup" class="bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700">{btn_texts[lang]["start"]}</a>\n            </nav>\n            <select onchange="window.location.href=\'/lang/\'+this.value+\'.html\'" class="md:hidden border rounded px-2 py-1 text-xs">\n' + 
        '                <option value="ko">🇰🇷 한국어</option>\n' +
        '                <option value="en">🇺🇸 English</option>\n' +
        '                <option value="zh-CN">🇨🇳 简体中文</option>\n' +
        '                <option value="zh-TW">🇹🇼 繁體中文</option>\n' +
        '                <option value="ja">🇯🇵 日本語</option>\n' +
        '                <option value="hi">🇮🇳 हिन्दी</option>\n' +
        '                <option value="es">🇪🇸 Español</option>\n' +
        '                <option value="fr">🇫🇷 Français</option>\n' +
        '                <option value="ar">🇸🇦 العربية</option>\n' +
        '                <option value="bn">🇧🇩 বাংলা</option>\n' +
        '                <option value="ru">🇷🇺 Русский</option>\n' +
        '                <option value="pt">🇧🇷 Português</option>\n' +
        f'            </select>',
        html
    )
    
    # 4. Hero 섹션 모바일 최적화
    html = re.sub(
        r'<section class="gradient-bg text-white py-16">',
        '<section class="gradient-bg text-white py-8 sm:py-16">',
        html
    )
    
    # Hero 타이틀 크기 축소
    html = re.sub(
        r'<h1 class="text-4xl md:text-5xl font-bold mb-4">',
        '<h1 class="text-2xl sm:text-4xl md:text-5xl font-bold mb-3 sm:mb-4">',
        html
    )
    
    # Hero 부제목 크기 축소
    html = re.sub(
        r'<p class="text-lg mb-8">',
        '<p class="text-sm sm:text-lg mb-6 sm:mb-8">',
        html
    )
    
    # 5. 버튼 URL 수정 및 1줄 배치
    # "무료로 시작하기" 버튼 (Hero 섹션)
    html = re.sub(
        r'<div class="flex flex-col sm:flex-row gap-4 justify-center">\s*<a href="#[^"]*" class="bg-white text-purple-600 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100">([^<]+)</a>',
        f'<div class="flex flex-row gap-2 sm:gap-4 justify-center max-w-md mx-auto">\n                <a href="/signup" class="flex-1 bg-white text-purple-600 px-4 sm:px-8 py-2 sm:py-3 rounded-lg font-semibold hover:bg-gray-100 text-xs sm:text-base mobile-btn">{btn_texts[lang]["start"]}</a>',
        html
    )
    
    # "데모 보기" 버튼 (Hero 섹션)
    html = re.sub(
        r'<a href="#[^"]*" class="bg-purple-700 text-white px-8 py-3 rounded-lg font-semibold hover:bg-purple-800">([^<]+)</a>',
        f'<a href="/demo" class="flex-1 bg-purple-700 text-white px-4 sm:px-8 py-2 sm:py-3 rounded-lg font-semibold hover:bg-purple-800 text-xs sm:text-base mobile-btn">{btn_texts[lang]["demo"]}</a>',
        html,
        count=1  # Hero 섹션의 첫 번째만 변경
    )
    
    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ {lang}.html 수정 완료")

print("\n✅ 모든 12개 언어 HTML 파일 수정 완료!")
print("   - 버튼 URL: /signup, /demo")
print("   - 모바일 최적화: 글자 축소, 버튼 1줄 배치")
print("   - 플랫폼 이름 축소: CallMind AI")
