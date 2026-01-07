#!/usr/bin/env python3
"""
남아있는 모든 한국어 텍스트를 완벽하게 번역
버튼, FAQ 질문 등 누락된 모든 부분 수정
"""

from pathlib import Path
import re

# 번역 맵핑
BUTTON_TRANSLATIONS = {
    'en': {
        '무료로 시작하기': 'Start for Free',
        '무료로 Get Started': 'Start for Free',
        '무료로': 'Free',
        '데모 보기': 'View Demo',
        '시작하기': 'Get Started',
        'AI가 대신하는 똑똑한 통화 비서': 'Your Smart AI Call Assistant',
        'AI驱动 智能通话助手': 'Your Smart AI Call Assistant',
        '무료로도 사용할 수 있나요?': 'Can I use it for free?'
    },
    'zh-CN': {
        '무료로 시작하기': '免费开始',
        '무료로 开始使用': '免费开始',
        '무료로': '免费',
        '데모 보기': '查看演示',
        '시작하기': '开始使用',
        'AI가 대신하는 똑똑한 통화 비서': 'AI代理 智能通话助手',
        'AI驱动 智能通话助手': 'AI代理 智能通话助手',
        '무료로도 사용할 수 있나요?': '可以免费使用吗?'
    },
    'zh-TW': {
        '무료로 시작하기': '免費開始',
        '무료로': '免費',
        '데모 보기': '觀看演示',
        '시작하기': '開始使用',
        'AI가 대신하는 똑똑한 통화 비서': 'AI代理 智能通話助手',
        '무료로도 사용할 수 있나요?': '可以免費使用嗎?'
    },
    'ja': {
        '무료로 시작하기': '無料で始める',
        '무료로 始める': '無料で始める',
        '무료로': '無料',
        '데모 보기': 'デモを見る',
        '시작하기': '始める',
        'AI가 대신하는 똑똑한 통화 비서': 'AIがサポート スマート通話アシスタント',
        '무료로도 사용할 수 있나요?': '無料で使えますか？'
    },
    'hi': {
        '무료로 시작하기': 'मुफ्त में शुरू करें',
        '무료로 शुरू करें': 'मुफ्त में शुरू करें',
        '무료로': 'मुफ्त',
        '데모 보기': 'डेमो देखें',
        '시작하기': 'शुरू करें',
        'AI가 대신하는 똑똑한 통화 비서': 'AI द्वारा संचालित स्मार्ट कॉल सहायक',
        '무료로도 사용할 수 있나요?': 'क्या मैं इसे मुफ्त में उपयोग कर सकता हूं?'
    },
    'es': {
        '무료로 시작하기': 'Comenzar gratis',
        '무료로 Comenzar': 'Comenzar gratis',
        '무료로': 'Gratis',
        '데모 보기': 'Ver demo',
        '시작하기': 'Comenzar',
        'AI가 대신하는 똑똑한 통화 비서': 'Tu asistente de llamadas inteligente con IA',
        '무료로도 사용할 수 있나요?': '¿Puedo usarlo gratis?'
    },
    'fr': {
        '무료로 시작하기': 'Commencer gratuitement',
        '무료로 Commencer': 'Commencer gratuitement',
        '무료로': 'Gratuit',
        '데모 보기': 'Voir la démo',
        '시작하기': 'Commencer',
        'AI가 대신하는 똑똑한 통화 비서': 'Votre assistant d\'appel intelligent avec IA',
        '무료로도 사용할 수 있나요?': 'Puis-je l\'utiliser gratuitement ?'
    },
    'ar': {
        '무료로 시작하기': 'ابدأ مجانًا',
        '무료로 ابدأ': 'ابدأ مجانًا',
        '무료로': 'مجاني',
        '데모 보기': 'عرض توضيحي',
        '시작하기': 'ابدأ',
        'AI가 대신하는 똑똑한 통화 비서': 'مساعد المكالمات الذكي بالذكاء الاصطناعي',
        '무료로도 사용할 수 있나요?': 'هل يمكنني استخدامه مجانًا؟'
    },
    'bn': {
        '무료로 시작하기': 'বিনামূল্যে শুরু করুন',
        '무료로 শুরू করুন': 'বিনামূল্যে শুরু করুন',
        '무료로': 'বিনামূল্যে',
        '데모 보기': 'ডেমো দেখুন',
        '시작하기': 'শুরু করুন',
        'AI가 대신하는 똑똑한 통화 비서': 'AI দ্বারা চালিত স্মার্ট কল সহায়ক',
        '무료로도 사용할 수 있나요?': 'আমি কি এটি বিনামূল্যে ব্যবহার করতে পারি?'
    },
    'ru': {
        '무료로 시작하기': 'Начать бесплатно',
        '무료로 Начать': 'Начать бесплатно',
        '무료로': 'Бесплатно',
        '데모 보기': 'Смотреть демо',
        '시작하기': 'Начать',
        'AI가 대신하는 똑똑한 통화 비서': 'Умный помощник для звонков с ИИ',
        '무료로도 사용할 수 있나요?': 'Могу ли я использовать его бесплатно?'
    },
    'pt': {
        '무료로 시작하기': 'Começar gratuitamente',
        '무료로 Começar': 'Começar gratuitamente',
        '무료로': 'Gratuito',
        '데모 보기': 'Ver demonstração',
        '시작하기': 'Começar',
        'AI가 대신하는 똑똑한 통화 비서': 'Seu assistente de chamadas inteligente com IA',
        '무료로도 사용할 수 있나요?': 'Posso usá-lo gratuitamente?'
    }
}

def fix_html_file(lang_code):
    """HTML 파일에서 남은 한국어 텍스트 수정"""
    html_file = Path(f'/home/user/webapp/public/lang/{lang_code}.html')
    
    if not html_file.exists():
        print(f"❌ 파일 없음: {html_file}")
        return False
    
    content = html_file.read_text(encoding='utf-8')
    original_content = content
    
    # 번역 맵에서 모든 한국어 텍스트 교체
    translations = BUTTON_TRANSLATIONS.get(lang_code, {})
    replaced_count = 0
    
    for korean_text, translated_text in translations.items():
        if korean_text in content:
            content = content.replace(korean_text, translated_text)
            replaced_count += 1
            print(f"  ✓ '{korean_text}' → '{translated_text}'")
    
    # 변경사항이 있으면 파일 저장
    if content != original_content:
        html_file.write_text(content, encoding='utf-8')
        print(f"✅ {lang_code}.html: {replaced_count}개 항목 수정 완료")
        return True
    else:
        print(f"✅ {lang_code}.html: 수정할 내용 없음")
        return True

def main():
    """메인 실행 함수"""
    print("=" * 70)
    print("남아있는 한국어 텍스트 완벽 번역")
    print("=" * 70)
    
    # 한국어 제외 10개 언어
    languages = ['en', 'zh-CN', 'zh-TW', 'ja', 'hi', 'es', 'fr', 'ar', 'bn', 'ru', 'pt']
    
    success_count = 0
    for lang_code in languages:
        print(f"\n[{lang_code}] 처리 중...")
        if fix_html_file(lang_code):
            success_count += 1
    
    print("\n" + "=" * 70)
    print(f"✅ 완료: {success_count}/{len(languages)}개 언어")
    print("=" * 70)

if __name__ == '__main__':
    main()
