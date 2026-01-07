#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
최종 완벽 번역 적용 - 12개 언어 × (모든 UI + FAQ 35개 + 산업별 6개 + 버튼 동작)
"""
import json
import re

# 한국어 HTML 읽기
with open('public/lang/ko.html', 'r', encoding='utf-8') as f:
    ko_html = f.read()

# 12개 언어 완전 번역 로드
with open('translations_all_11.json', 'r', encoding='utf-8') as f:
    TRANS = json.load(f)

# 한국어 FAQ 로드
with open('faq_korean.json', 'r', encoding='utf-8') as f:
    faq_ko = json.load(f)

print(f"✅ 한국어 HTML 및 FAQ {len(faq_ko)}개 로드 완료")
print(f"✅ {len(TRANS)}개 언어 번역 데이터 로드 완료")

# 모든 언어에 대해 HTML 생성
for lang_code, trans in TRANS.items():
    print(f"\n처리 중: {lang_code} ({trans['name']})")
    
    # 한국어 HTML을 복사하여 시작
    html = ko_html
    
    # 1. lang 속성 변경
    html = re.sub(r'<html lang="ko">', f'<html lang="{lang_code}">', html)
    
    # 2. 페이지 제목 변경
    html = re.sub(
        r'<title>CallMind AI - AI 통화비서 플랫폼</title>',
        f'<title>{trans["page_title"]}</title>',
        html
    )
    
    # 3. 히어로 섹션 번역
    html = re.sub(
        r'AI가 대신하는<br>똑똑한 통화 비서',
        trans['hero_title'],
        html
    )
    html = re.sub(
        r'전화·음성·메신저 대화를 AI가 실시간으로 응대·요약·기록·분석',
        trans['hero_subtitle'],
        html
    )
    
    # 4. 버튼을 <a> 앵커 링크로 변경 (실제 동작)
    # "무료로 시작하기" 버튼
    html = re.sub(
        r'<button class="([^"]*?)">.*?무료로 시작하기.*?</button>',
        f'<a href="#pricing" class="\\1">{trans["btn_start"]}</a>',
        html,
        flags=re.DOTALL
    )
    
    # "데모 보기" 버튼
    html = re.sub(
        r'<button class="([^"]*?)">.*?데모 보기.*?</button>',
        f'<a href="#features" class="\\1">{trans["btn_demo"]}</a>',
        html,
        flags=re.DOTALL
    )
    
    # 5. 통계 섹션 번역
    html = re.sub(r'<div class="text-xs text-white/80">지원 언어</div>', 
                  f'<div class="text-xs text-white/80">{trans["stat1"]}</div>', html)
    html = re.sub(r'<div class="text-xs text-white/80">인식 정확도</div>', 
                  f'<div class="text-xs text-white/80">{trans["stat2"]}</div>', html)
    html = re.sub(r'<div class="text-xs text-white/80">무중단 서비스</div>', 
                  f'<div class="text-xs text-white/80">{trans["stat3"]}</div>', html)
    html = re.sub(r'<div class="text-xs text-white/80">응답 속도</div>', 
                  f'<div class="text-xs text-white/80">{trans["stat4"]}</div>', html)
    
    # 6. 헤더 메뉴 번역
    html = re.sub(r'<a href="#features" class="([^"]*?)">핵심 기능</a>',
                  f'<a href="#features" class="\\1">{trans["header_core"]}</a>', html)
    html = re.sub(r'<a href="#industry" class="([^"]*?)">산업별 특화</a>',
                  f'<a href="#industry" class="\\1">{trans["header_industry"]}</a>', html)
    html = re.sub(r'<a href="#pricing" class="([^"]*?)">요금제</a>',
                  f'<a href="#pricing" class="\\1">{trans["header_pricing"]}</a>', html)
    
    # 7. 챗봇 제목 번역
    html = re.sub(
        r'<div class="font-semibold text-sm">FAQ 도우미</div>',
        f'<div class="font-semibold text-sm">{trans["chatbot_title"]}</div>',
        html
    )
    html = re.sub(
        r'<div class="text-xs text-purple-200">자주 묻는 질문</div>',
        f'<div class="text-xs text-purple-200">{trans["chatbot_subtitle"]}</div>',
        html
    )
    
    # 8. FAQ 카테고리 번역
    categories = [
        ('기본 서비스 안내', trans['cat1']),
        ('통화 녹취·요약 기능', trans['cat2']),
        ('AI 협상 비서 관련', trans['cat3']),
        ('보안·법적', trans['cat4']),
        ('요금·운영', trans['cat5']),
        ('계약·업무 자동화', trans['cat6']),
        ('AI to AI 통화', trans['cat7']),
        ('다국어·글로벌', trans['cat8'])
    ]
    
    for ko_cat, trans_cat in categories:
        html = re.sub(
            f'<i class="fas fa-[^"]*? mr-1 text-xs"></i>{ko_cat}',
            f'<i class="fas fa-circle mr-1 text-xs"></i>{trans_cat}',
            html
        )
    
    # 9. FAQ 질문/답변 번역 (언어에 faq 데이터가 있는 경우만)
    if 'faq' in trans and trans['faq']:
        for i, faq_item in enumerate(trans['faq'], 1):
            # 질문 번역
            ko_q = faq_ko[i-1]['question'] if i <= len(faq_ko) else ''
            if ko_q:
                html = re.sub(
                    f'<span>{re.escape(ko_q)}</span>',
                    f'<span>{faq_item["q"]}</span>',
                    html
                )
            
            # 답변 번역
            ko_a = faq_ko[i-1]['answer'] if i <= len(faq_ko) else ''
            if ko_a:
                # 답변이 포함된 div 찾아서 변경
                pattern = f'<div class="faq-answer">\\s*{re.escape(ko_a)}\\s*</div>'
                replacement = f'<div class="faq-answer">\n                        {faq_item["a"]}\n                    </div>'
                html = re.sub(pattern, replacement, html)
    
    # 10. 산업별 특화 섹션 번역
    industries = {
        '간병인': {
            'title': {
                'ko': '간병인', 'en': 'Caregiving', 'zh-CN': '护理', 'zh-TW': '護理', 
                'ja': '介護', 'hi': 'देखभाल', 'es': 'Cuidado', 'fr': 'Soins', 
                'ar': 'الرعاية', 'bn': 'যত্ন', 'ru': 'Уход', 'pt': 'Cuidados'
            },
            'desc': {
                'ko': '보호자 통화 자동 요약, 응급 상황 감지', 
                'en': 'Auto-summarize caregiver calls, detect emergencies',
                'zh-CN': '自动总结护理电话，检测紧急情况',
                'zh-TW': '自動總結護理電話，檢測緊急情況',
                'ja': '介護者通話を自動要約、緊急事態を検出',
                'hi': 'देखभालकर्ता कॉल का स्वतः सारांश, आपात स्थिति का पता लगाएं',
                'es': 'Resumir automáticamente llamadas de cuidadores, detectar emergencias',
                'fr': 'Résumer automatiquement les appels des soignants, détecter les urgences',
                'ar': 'تلخيص تلقائي لمكالمات مقدمي الرعاية، اكتشاف حالات الطوارئ',
                'bn': 'যত্নশীল কলের স্বতঃ সারাংশ, জরুরী অবস্থা সনাক্ত করুন',
                'ru': 'Автоматическое резюмирование звонков опекунов, обнаружение чрезвычайных ситуаций',
                'pt': 'Resumir automaticamente chamadas de cuidadores, detectar emergências'
            }
        },
        '건설현장': {
            'title': {
                'ko': '건설현장', 'en': 'Construction Sites', 'zh-CN': '建筑工地', 'zh-TW': '建築工地',
                'ja': '建設現場', 'hi': 'निर्माण स्थल', 'es': 'Sitios de Construcción', 'fr': 'Chantiers de Construction',
                'ar': 'مواقع البناء', 'bn': 'নির্মাণ সাইট', 'ru': 'Строительные Площадки', 'pt': 'Canteiros de Obras'
            },
            'desc': {
                'ko': '작업 중 통화 대신 AI 응대, 안전 우선',
                'en': 'AI handles calls during work, safety first',
                'zh-CN': 'AI在工作期间处理电话，安全第一',
                'zh-TW': 'AI在工作期間處理電話，安全第一',
                'ja': '作業中はAIが通話対応、安全優先',
                'hi': 'काम के दौरान AI कॉल संभालता है, सुरक्षा पहले',
                'es': 'AI maneja llamadas durante el trabajo, seguridad primero',
                'fr': 'L\'IA gère les appels pendant le travail, sécurité d\'abord',
                'ar': 'الذكاء الاصطناعي يتعامل مع المكالمات أثناء العمل، السلامة أولاً',
                'bn': 'কাজের সময় AI কল পরিচালনা করে, নিরাপত্তা প্রথম',
                'ru': 'ИИ обрабатывает звонки во время работы, безопасность прежде всего',
                'pt': 'IA lida com chamadas durante o trabalho, segurança em primeiro lugar'
            }
        },
        '택배·배송': {
            'title': {
                'ko': '택배·배송', 'en': 'Delivery Services', 'zh-CN': '配送服务', 'zh-TW': '配送服務',
                'ja': '配送サービス', 'hi': 'डिलीवरी सेवाएं', 'es': 'Servicios de Entrega', 'fr': 'Services de Livraison',
                'ar': 'خدمات التوصيل', 'bn': 'ডেলিভারি সেবা', 'ru': 'Службы Доставки', 'pt': 'Serviços de Entrega'
            },
            'desc': {
                'ko': '운전 중 안전 통화, 반복 문의 자동 처리',
                'en': 'Safe calls while driving, auto-handle repeat inquiries',
                'zh-CN': '驾驶时安全通话，自动处理重复查询',
                'zh-TW': '駕駛時安全通話，自動處理重複查詢',
                'ja': '運転中の安全通話、繰り返しの問い合わせを自動処理',
                'hi': 'ड्राइविंग के दौरान सुरक्षित कॉल, दोहराई जाने वाली पूछताछ को स्वतः संभालें',
                'es': 'Llamadas seguras mientras conduce, manejar automáticamente consultas repetidas',
                'fr': 'Appels sécurisés en conduisant, gérer automatiquement les demandes répétées',
                'ar': 'مكالمات آمنة أثناء القيادة، معالجة الاستفسارات المتكررة تلقائياً',
                'bn': 'গাড়ি চালানোর সময় নিরাপদ কল, পুনরাবৃত্তি জিজ্ঞাসা স্বয়ংক্রিয়ভাবে পরিচালনা করুন',
                'ru': 'Безопасные звонки за рулем, автоматическая обработка повторяющихся запросов',
                'pt': 'Chamadas seguras ao dirigir, lidar automaticamente com consultas repetidas'
            }
        },
        '자영업': {
            'title': {
                'ko': '자영업', 'en': 'Self-Employed', 'zh-CN': '自雇', 'zh-TW': '自僱',
                'ja': '自営業', 'hi': 'स्व-नियोजित', 'es': 'Autónomos', 'fr': 'Travailleurs Indépendants',
                'ar': 'العمل الحر', 'bn': 'স্ব-কর্মসংস্থান', 'ru': 'Самозанятые', 'pt': 'Autônomos'
            },
            'desc': {
                'ko': '예약 접수, 고객 문의 자동 처리',
                'en': 'Auto-handle reservations and customer inquiries',
                'zh-CN': '自动处理预订和客户查询',
                'zh-TW': '自動處理預訂和客戶查詢',
                'ja': '予約受付、顧客問い合わせを自動処理',
                'hi': 'आरक्षण और ग्राहक पूछताछ को स्वतः संभालें',
                'es': 'Manejar automáticamente reservas y consultas de clientes',
                'fr': 'Gérer automatiquement les réservations et les demandes des clients',
                'ar': 'معالجة الحجوزات واستفسارات العملاء تلقائياً',
                'bn': 'স্বয়ংক্রিয়ভাবে রিজার্ভেশন এবং গ্রাহক জিজ্ঞাসা পরিচালনা করুন',
                'ru': 'Автоматическая обработка бронирований и запросов клиентов',
                'pt': 'Lidar automaticamente com reservas e consultas de clientes'
            }
        },
        '프리랜서·영업': {
            'title': {
                'ko': '프리랜서·영업', 'en': 'Freelancers', 'zh-CN': '自由职业者', 'zh-TW': '自由職業者',
                'ja': 'フリーランサー', 'hi': 'फ्रीलांसर', 'es': 'Autónomos', 'fr': 'Freelancers',
                'ar': 'العمل الحر', 'bn': 'ফ্রিল্যান্সার', 'ru': 'Фрилансеры', 'pt': 'Freelancers'
            },
            'desc': {
                'ko': '통화 분석, 협상 전략, 고객 관리',
                'en': 'Call analysis, negotiation strategy, customer management',
                'zh-CN': '通话分析、谈判策略、客户管理',
                'zh-TW': '通話分析、談判策略、客戶管理',
                'ja': '通話分析、交渉戦略、顧客管理',
                'hi': 'कॉल विश्लेषण, बातचीत की रणनीति, ग्राहक प्रबंधन',
                'es': 'Análisis de llamadas, estrategia de negociación, gestión de clientes',
                'fr': 'Analyse des appels, stratégie de négociation, gestion des clients',
                'ar': 'تحليل المكالمات، استراتيجية التفاوض، إدارة العملاء',
                'bn': 'কল বিশ্লেষণ, আলোচনার কৌশল, গ্রাহক ব্যবস্থাপনা',
                'ru': 'Анализ звонков, стратегия переговоров, управление клиентами',
                'pt': 'Análise de chamadas, estratégia de negociação, gerenciamento de clientes'
            }
        },
        '공장·제조': {
            'title': {
                'ko': '공장·제조', 'en': 'Manufacturing', 'zh-CN': '制造', 'zh-TW': '製造',
                'ja': '製造', 'hi': 'विनिर्माण', 'es': 'Manufactura', 'fr': 'Fabrication',
                'ar': 'التصنيع', 'bn': 'উৎপাদন', 'ru': 'Производство', 'pt': 'Manufatura'
            },
            'desc': {
                'ko': '설비 이상 감지, 교대 인수인계',
                'en': 'Detect equipment issues, shift handover',
                'zh-CN': '检测设备问题，交接班',
                'zh-TW': '檢測設備問題，交接班',
                'ja': '設備異常検出、シフト引継ぎ',
                'hi': 'उपकरण समस्याओं का पता लगाएं, शिफ्ट हैंडओवर',
                'es': 'Detectar problemas de equipo, cambio de turno',
                'fr': 'Détecter les problèmes d\'équipement, passation de relève',
                'ar': 'اكتشاف مشاكل المعدات، تسليم الوردية',
                'bn': 'সরঞ্জাম সমস্যা সনাক্ত করুন, শিফট হস্তান্তর',
                'ru': 'Обнаружение проблем с оборудованием, передача смены',
                'pt': 'Detectar problemas de equipamento, passagem de turno'
            }
        }
    }
    
    # 산업별 섹션 번역 적용
    for ko_name, translations in industries.items():
        if lang_code in translations['title']:
            # 제목 번역
            pattern = f'<h3 class="font-bold text-gray-900 mb-1">{ko_name}</h3>'
            replacement = f'<h3 class="font-bold text-gray-900 mb-1">{translations["title"][lang_code]}</h3>'
            html = html.replace(pattern, replacement)
            
            # 설명 번역
            if ko_name in ['간병인', '건설현장', '택배·배송', '자영업', '프리랜서·영업', '공장·제조']:
                ko_desc = translations['desc']['ko']
                trans_desc = translations['desc'][lang_code]
                pattern = f'<p class="text-gray-600 mb-2">{ko_desc}</p>'
                replacement = f'<p class="text-gray-600 mb-2">{trans_desc}</p>'
                html = html.replace(pattern, replacement)
    
    # 파일 저장
    output_path = f'public/lang/{lang_code}.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ {lang_code}.html 완료")

print(f"\n✅ 모든 {len(TRANS)}개 언어 HTML 생성 완료!")
